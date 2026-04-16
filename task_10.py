import time
import functools
from collections import deque
import threading


def throttle(max_calls: int, period: float, timeout: float):
    """
    Decorator to limit the number of function calls within a time window and the execution time.

    Args:
        max_calls: Maximum allowed calls in the specified period.
        period: Time window in seconds.
        timeout: Maximum allowed execution time for a single call in seconds.

    Raises:
        TimeoutError: If function execution exceeds timeout.
        RuntimeError: If call limit is exceeded.
    """

    def decorator(func):
        call_times = deque()
        lock = threading.Lock()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_times

            current_time = time.time()

            with lock:
                while call_times and current_time - call_times[0] > period:
                    call_times.popleft()

                if len(call_times) >= max_calls:
                    raise RuntimeError(
                        f"Rate limit exceeded for {func.__name__}. "
                        f"Max {max_calls} calls per {period} seconds."
                    )

                call_times.append(current_time)


            result = [None]
            exception = [None]

            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    exception[0] = e

            thread = threading.Thread(target=target)
            thread.start()
            thread.join(timeout)

            if thread.is_alive():
                # Timeout occurred
                raise TimeoutError(
                    f"Function '{func.__name__}' execution exceeded timeout of {timeout} seconds."
                )

            if exception[0]:
                raise exception[0]

            return result[0]

        return wrapper

    return decorator



@throttle(max_calls=3, period=10, timeout=2)
def slow_api_call(value):
    print(f"Processing {value}...")
    time.sleep(1)
    return f"Result: {value}"


if __name__ == "__main__":
    for i in range(5):
        try:
            print(slow_api_call(i))
        except (RuntimeError, TimeoutError) as e:
            print(f"Error: {e}")
        time.sleep(0.5)
