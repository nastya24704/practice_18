import json

def sort_list(json_string: str) -> list:
    """
    Parse a JSON string of lists [str, num] and sort them by number in non-ascending order.

    Args:
        json_string: String literal in JSON format (list of lists).

    Returns:
        Sorted list of lists.
    """
    data = json.loads(json_string)
  
    sorted_data = sorted(data, key=lambda item: item[1], reverse=True)
    return sorted_data


if __name__ == "__main__":
    input_json = '[["apple", 5], ["banana", 2], ["cherry", 10], ["date", 2]]'
    result = sort_list(input_json)
    print(f"Sorted: {result}")
