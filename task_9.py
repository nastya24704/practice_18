import json
import functools

def to_format(format_type=None):
    """
    Decorator to convert function return value to JSON, XML, or YAML.

    Args:
        format_type: 'json', 'xml', 'yaml'. Defaults to 'json' if None.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            target_format = format_type or "json"
            
            if target_format == "json":
                return json.dumps(data, ensure_ascii=False, default=str)
            
            elif target_format == "xml":
                try:
                    import dicttoxml
                    return dicttoxml.dicttoxml(data).decode()
                except ImportError:
                    return f"<error>dicttoxml not installed. Data: {data}</error>"
            
            elif target_format == "yaml":
                try:
                    import yaml
                    return yaml.dump(data, allow_unicode=True)
                except ImportError:
                    return f"Error: PyYAML not installed. Data: {data}"
            else:
                raise ValueError(f"Unsupported format: {target_format}")
                
        return wrapper
    return decorator


@to_format()
def get_user():
    return {"id": 1, "name": "Nastya"}

@to_format("xml")
def get_items():
    return ["apple", "banana", "cherry"]

if __name__ == "__main__":
    print("JSON:", get_user())
    print("XML:", get_items())
