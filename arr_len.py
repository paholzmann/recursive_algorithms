
def recursive_arr_len(arr):
    """
    Recursively calculates the number of elements in a list.

    This function determines the length of the list by recursively
    removing the first element and adding 1 for each recursive step
    until the list is empty.
    
    Parameters:
        arr (list): A list containing elements of any data type.

    Returns:
        int: The number of elements in a list.

    Raises:
        TypeError: If the input is not a list.
    
    Example:
        >>> recursive_arr_len([2,5,7])
        3
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if len(arr) == 0:
        return 0
    return 1 + recursive_arr_len(arr[1:])

arr = [2,5,7]
print(recursive_arr_len(arr=arr))
