def print_result_single_arg(func):
    """
    Decorator that prints the result of a function that takes exactly one argument.
    """
    def wrapper(arg):
        result = func(arg)
        print(result)
        return result
    return wrapper


@print_result_single_arg
def square(x):
    return x * x

@print_result_single_arg
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    square(5)  
    greet("nastya") 
