def my_decorator(func: callable) -> callable:
    """
    A function that serves as a wrapper for another function.

    This function is responsible for printing a message before the wrapped function is called,
    calling the wrapped function, and printing a message after the wrapped function is called.

    Parameters:
        None

    Returns:
        None
    """
    def wrapper(*args, **kwargs) -> None:
        """
        A function that prints a message before and after calling another function.
        No parameters are passed in. The function does not return anything.
        """
        print("Something is happening before the function is called.")
        res = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return res
    return wrapper


@my_decorator
def say_hello(a: int, b: int)-> int:
    """
    Parameters:
        a: int
        b: int
    A function that prints "Hello!" and returns the sum of two numbers.

    """
    print("Hello!")
    return a + b

print(say_hello(5,3))