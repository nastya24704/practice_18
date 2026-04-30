def count_uppercase_from_to(s: str, i: int, j: int) -> int:
    """
    Returns the number of uppercase characters in the string
    from position i to j inclusive (1-based indexing).
    """
    return len(list(filter(lambda char: char.isupper(), s[i - 1:j])))


text = input("Anastasiya Elizaveta Vladimir")
start, end = int(input()), int(input())
result = count_uppercase_from_to(text, start, end)
print(result)
