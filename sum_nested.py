
def sum_nested(arr):
    """
    Recursively calculates the sum of all numeric elements in a possibly nested list.

    Parameters:
        arr (list): A possibly nested list only containing numeric values.
    
    Returns:
        int | float: The sum of all numeric values inside the nested list.

    Raises:
        TypeError: If the input is not a list.
    
    Example:
        >>> sum_nested([1, [2, [3, 4], 5], 6])
        21
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if len(arr) == 0:
        return 0
    if isinstance(arr[0], list):
        return sum_nested(arr[0]) + sum_nested(arr[1:])
    else:
        return arr[0] + sum_nested(arr[1:])
    
arr = [1, [2, [3, 4], 5], 6]
print(sum_nested(arr=arr))
