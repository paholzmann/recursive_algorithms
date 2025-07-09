
def binary_search(arr, x, left, right):
    """
    Recursively performs binary search to find the index of a target element in a sorted list.

    Parameters:
        arr (list): A sorted list of comparable elements.
        x (any): The target element to search for.
        left (int): The starting index of the current search range.
        right (int): The ending index of the current search range.

    Returns:
        int or str: The index of the target element if found, otherwise 'Not found.'

    Raises:
        TypeError: If the input is not a list.

    Example:
        >>> binary_search([1, 2, 3, 4, 5, 6], x=2, left=0, right=5)
        1
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if left > right:
        return "Not found."
    middle = (left + right) // 2
    if arr[middle] == x:
        return middle
    elif x < arr[middle]:
        return binary_search(arr, x, left, middle - 1)
    elif x > arr[middle]:
        return binary_search(arr, x, middle + 1, right)
    
arr = [1, 2, 3, 4, 5, 6]
print(binary_search(arr=arr, x=2, left=0, right=len(arr) - 1))
