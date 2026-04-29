def count_ending_with(start: int, end: int, divisor: int, last_digit: int) -> int:
    """
    Count natural numbers in [start, end] that are NOT multiples of divisor and end with last_digit.

    Args:
        start: Lower bound (inclusive).
        end: Upper bound (inclusive).
        divisor: The number should not be divisible by this.
        last_digit: The required last digit (0-9).

    Returns:
        The count of matching numbers.
    """
    lower_bound = max(start, 1)
    numbers = range(lower_bound, end + 1)
    
    matches = map(lambda x: 1 if (x % divisor != 0) and (x % 10 == last_digit) else 0, numbers)
    return sum(matches)


if __name__ == "__main__":
    a, b, c, d = int(input("start")), int(input("end")), int(input(dicisor)), int(input(last_digit))
    result = count_ending_with(a, b, c, d)
    print(result)
