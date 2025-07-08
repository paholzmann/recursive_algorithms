
def recursive_sum(n):
    """
    Recursively calculates the sum of all integers from 1 to n.

    The function sums up all integers starting from 1 up to the given number n 
    by recursively adding n to the sum of all integers from 1 to n-1.

    Parameters:
        n (int): A positive integer (n >= 1). Sets the upper bound of the summation.

    Returns:
        int: The sum of all integers from 1 to n.
    
    Raises:
        ValueError: If n is negative.
    
    Example:
        >>> recursive_sum(25)
        325
    """
    if n < 0:
        raise ValueError("Number cannot be negative.")
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)


print(recursive_sum(25))
