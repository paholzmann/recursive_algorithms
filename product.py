
def recursive_product(arr):
    """
    Recursively calculates the product of all numbers in a list.

    The function multiplies all elements of the input list by recursively 
    multiplying the first element with the product of the remaining elements.
    For an empty list, the product is defined as 1 (multiplicative identity).

    Parameters:
        arr (list of int or float): A list of numbers.

    Returns:
        int or float: The product of all numbers in the list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.

    Example:
        >>> recursive_product([2, 3, 4])
        24
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if len(arr) == 0:
        return 1
    return arr[0] * recursive_product(arr[1:])


arr = [2, 3, 4]
print(recursive_product(arr=arr))
