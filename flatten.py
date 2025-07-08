
def recursive_flatten(arr):
    """
    Recursively flattens a nested list into a single-level list.

    This function takes a list that may contain nested lists at any depth and 
    returns a new list with all elements flattened into a single list.

    Parameters:
        arr (list): A list potentially containing nested lists and elements of any data type.

    Returns:
        list: A flattened list containing all elements from the nested structure.

    Raises:
        TypeError: If the input is not a list.

    Example:
        >>> recursive_flatten([1, [2, [3, 4], 5], 6])
        [1, 2, 3, 4, 5, 6]
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if len(arr) == 0:
        return []
    if isinstance(arr[0], list):
        return recursive_flatten(arr[0]) + recursive_flatten(arr[1:])
    else:
        return [arr[0]] + recursive_flatten(arr[1:])

arr = [1, [2, [3, 4], 5], 6]
print(recursive_flatten(arr=arr))
