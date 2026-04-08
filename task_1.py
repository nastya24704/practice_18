def count_uppercase_from_to(s: str, i: int, j: int) -> int:
    """
    Returns the number of uppercase characters in the string
    from position i to j inclusive (1-based indexing).
    """
    return len(list(filter(lambda char: char.isupper(), s[i - 1:j])))


text = "Anastasiya Elizaveta Vladimir"
result = count_uppercase_from_to(text, 1, 10)
print(result)
