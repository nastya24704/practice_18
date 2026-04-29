def sum_multiples_of_both(start: int, end: int, divisor1: int, divisor2: int) -> int:
    """
    Calculate the sum of natural numbers in [start, end] that are multiples of both divisor1 and divisor2.

    Args:
        start: Lower bound of the interval (inclusive).
        end: Upper bound of the interval (inclusive).
        divisor1: First divisor.
        divisor2: Second divisor.

    Returns:
        The sum of numbers divisible by both divisors.
    """
   
    lower_bound = max(start, 1)
    numbers = range(lower_bound, end + 1)
    
    filtered_numbers = filter(lambda x: x % divisor1 == 0 and x % divisor2 == 0, numbers)
    return sum(filtered_numbers)


if __name__ == "__main__":
    a, b, c, d = 1, 30, 3, 5
    print(sum_multiples_of_both(a, b, c, d))
