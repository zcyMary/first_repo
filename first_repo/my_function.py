def my_function() -> None:
    print("Hello from my_function!")


def multiply(a: int | float, b: int | float) -> int | float:
    """
    This function takes two arguments, a and b, and returns their product.

    Parameters:
        a (int or float): The first number to multiply.
        b (int or float): The second number to multiply.

    Returns:
        int or float: The product of a and b.
    """
    return a * b
