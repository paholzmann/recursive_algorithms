

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n recursively.

    The factorial of n (denoted as n!) is the product of all positive integers 
    less than or equal to n. By definition, factorial(0) is 1.

    Parameters:
        n (int): A non-negative integer (n >= 0).

    Returns:
        int: The factorial of the input number n.

    Raises:
        ValueError: If n is a negative integer.

    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Number cannot be negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) 
