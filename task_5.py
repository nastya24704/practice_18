from functools import reduce
import math

def product_of_square(start: int, end: int, divisor: int) -> int:
    """
    Calculate the product of natural numbers in [start, end] that are perfect squares and multiples of divisor.

    Args:
        start: Lower bound (inclusive).
        end: Upper bound (inclusive).
        divisor: The required divisor.

    Returns:
        The product of matching numbers. Returns 1 if none found (identity for multiplication).
    """
    lower_bound = max(start, 1)
    numbers = range(lower_bound, end + 1)
    
    
    def is_perfect_square(n: int) -> bool:
        root = math.isqrt(n)
        return root * root == n

    filtered_nums = filter(lambda x: is_perfect_square(x) and x % divisor == 0, numbers)
    
    
    product = reduce(lambda x, y: x * y, filtered_nums, 1)
    return product


if __name__ == "__main__":
    a, b, c = int(input('start')), int(input('end')), int(input('divisor'))
    result = product_of_square(a, b, c)
    print(result)
