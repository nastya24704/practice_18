import functools
from datetime import datetime

def log_exceptions(log_filename="errors.log"):
    """
    Decorator that logs exceptions (date, time, type) to a specified file.
    
    Args:
        log_filename: Path to the log file.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                with open(log_filename, "a", encoding="utf-8") as log_file:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log_file.write(f"[{timestamp}] Function '{func.__name__}' raised {type(e).__name__}: {e}\n")
                
                raise
        return wrapper
    return decorator

# Example usage
@log_exceptions("app_errors.log")
def divide(a, b):
    return a / b

@log_exceptions()
def parse_int(s):
    return int(s)

if __name__ == "__main__":
    try:
        divide(10, 0)
    except ZeroDivisionError:
        pass
    
    try:
        parse_int("abc")
    except ValueError:
        pass
    
    print("Check the log file for recorded exceptions.")
