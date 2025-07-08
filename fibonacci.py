
def fibonacci(n):
    """
    Calculate the n-th Fibonacci number recursively.

    The Fibonacci sequence is a series of numbers where each number is the sum 
    of the two preceding ones, starting from 0 and 1. By definition,
    fibonacci(0) is 0 and fibonacci(1) is 1.

    Parameters:
        n (int): A non-negative integer (n >= 0).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.

    Example:
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("Number cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
