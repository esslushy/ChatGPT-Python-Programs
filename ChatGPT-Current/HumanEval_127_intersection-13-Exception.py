from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    >>> intersection((1, 2), (2, 3))
    'NO'
    >>> intersection((-1, 1), (0, 4))
    'NO'
    >>> intersection((-3, -1), (-5, 5))
    'YES'
    """
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    start1, end1 = interval1
    start2, end2 = interval2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    if intersection_start > intersection_end:
        return "NO"
    intersection_length = intersection_end - intersection_start + 1
    if is_prime(intersection_length):
        return "YES"
    return "NO"

def check(candidate):
    assert candidate((1, 2), (2, 3)) == 'NO'
    assert candidate((-1, 1), (0, 4)) == 'NO'
    assert candidate((-3, -1), (-5, 5)) == 'YES'
    assert candidate((-2, 2), (-4, 0)) == 'YES'
    assert candidate((-11, 2), (-1, -1)) == 'NO'
    assert candidate((1, 2), (3, 5)) == 'NO'
    assert candidate((1, 2), (1, 2)) == 'NO'
    assert candidate((-2, -2), (-3, -2)) == 'NO'

def test_check():
    check(intersection)

test_check()
