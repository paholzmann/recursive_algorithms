
def recursive_reverse(arr):
    """
    Recursively reverses the elements of a list.

    This function takes a list of any data type and returns a new list with the 
    elements in reversed order, using recursion.

    Parameters:
        arr (list): The list to be reversed.

    Returns:
        list: A new list containing the elements of `arr` in reverse order.

    Raises:
        TypeError: If the input is not a list.

    Example:
        >>> recursive_reverse([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1]
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if len(arr) == 0:
        return arr
    return recursive_reverse(arr[1:]) + [arr[0]]


arr = [1, 2, 3, 4, 5]
print(recursive_reverse(arr=arr))
