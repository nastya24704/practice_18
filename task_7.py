import json

def to_json(func):
    """
    Decorator that converts the function's return value to JSON format.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, ensure_ascii=False)
    return wrapper


@to_json
def get_dict(name, age):
    return {"name": name, "age": age}

@to_json
def get_list():
    return [1, 2, 3]


if __name__ == "__main__":
    print(get_dict("Nastya", 20))
    print(get_list())
