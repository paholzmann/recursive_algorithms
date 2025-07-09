
def count_flatten(arr):
    """
    Recursively counts all numeric elements in a nested list.

    Parameters:
        arr (list): A possibly nested list of elements containing all data types.
    
    Returns:
        int: Total number of elements found recursively.

    Raises:
        TypeError: If input is not a list.
    
    Example:
        >>> count_flatten([1, [2, [3, 4], 5], 6])
        6
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if len(arr) == 0:
        return 0
    if isinstance(arr[0], list):
        return count_flatten(arr[0]) + count_flatten(arr[1:])
    else:
        return 1 + count_flatten(arr[1:])

arr = [1, [2, [3, 4], 5], 6]
print(count_flatten(arr=arr))
