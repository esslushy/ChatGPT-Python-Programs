from typing import List

def can_arrange(arr: List[int]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """
    n = len(arr)
    
    # check the rightmost element
    if arr[n - 1] < arr[n - 2]:
        return n - 1
    
    # iterate from right to left and find the largest index
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            return i
    return -1

def check(candidate):
    assert candidate([1, 2, 4, 3, 5]) == 3
    assert candidate([1, 2, 4, 5]) == -1
    assert candidate([1, 4, 2, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate([4, 8, 5, 7, 3]) == 4
    assert candidate([]) == -1

def test_check():
    check(can_arrange)

test_check()