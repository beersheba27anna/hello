from typing import Callable, Sequence
from bisect import bisect_left, bisect_right
from math import sqrt

def __find_range_index(numbers: Sequence[int], in_range: range|None = None):
    index_left, index_right = (0, len(numbers))\
        if in_range is None else (0, 0)
    if in_range is not None and len(in_range) > 0:
        start, stop = (in_range[0], in_range[-1]) if in_range.step > 0 else\
            (in_range[-1], in_range[0])
        index_left = bisect_left(numbers, start)
        index_right = bisect_right(numbers, stop)
    return index_left, index_right


def get_all_range(numbers: Sequence[int], allowed: range|None = None)->list[int]:
    """
    numbers - sorted list of numbers in ascending order
    allowed - range of numbers (may be empty)
        returns list of numbers that greater or equal minimal value of range and less than maximal value
    for empty range the function returns the empty list
    for missed second argument the function returns the same "numbers"
    """
    index_left, index_right = __find_range_index(numbers, allowed)
    return list(numbers[index_left:index_right])


def get_all_not_in_range(numbers: Sequence[int], disallowed: range) -> list[int] :
    """
    numbers - sorted list of numbers in ascending order
    disallowed - range of numbers (may be empty)
        returns list of numbers from "numbers" that are not in a given range
    """
    index_left, index_right = __find_range_index(numbers, disallowed)
    result: list[int] = []
    middle = []
    if abs(disallowed.step) != 1:
        middle = [num for num in numbers[index_left:index_right]\
            if (num - disallowed.start) % disallowed.step != 0]
    result = list(numbers[:index_left]) + middle +\
        list(numbers[index_right:])
    return result



def my_sorted[T, K](items: Sequence[T],/,*, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    "items" is divided on the parts, each of which contains sqrt(len(items)) items
    Each part should be sorted separately by bubble sorting algorithm that you have already implemented
    After that all parts should be merged.
    No limitations for extra space
    Note: To use "sqrt" function from the module "math". This function returns float type
        so you should apply function "int" and the last part may contain more items
    """
    pass