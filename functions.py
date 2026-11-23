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

def __move_max_by_key_to_end[T](
        indices: list[int], keys: list[T], stop: int) -> int:
    """
    - indices - list with integer indices of elements in keys list
    - keys - a corresponding key to a specific value in original sequence being sorted
    - stop - index where to stop sorting
    - moves maximum element (by corresponding key) of the list to the end, ending is defined by the index stop
    - returns int value index of minimum position participating in the last exchange
        returns -1 with no exchange happening
    """
    last_exchange_index = -1
    for index in range(stop):
        if keys[indices[index]] > keys[indices[index+1]]: # type: ignore
            indices[index], indices[index+1] = indices[index+1], indices[index]
            last_exchange_index = index
    return last_exchange_index


def __bubble_sort_values_by_keys[K](
        keys: list[K], key_prefix: int = 0) -> list[int]:
    """
    Bubble sort algorithm returning indices of the elements
    to sort the keys in ascending order
    key_prefix - desired index start position
    """
    indices = list(range(len(keys)))
    unsorted_end = len(keys) - 1
    while unsorted_end > 0:
        unsorted_end = __move_max_by_key_to_end(
            indices, keys, unsorted_end)
    return [ind+key_prefix for ind in indices]


def merge_sorted_lists[K](
        blocks: list[list[int]], key_list:list[K]) -> list[int]:
    num_blocks = len(blocks)
    indices = [0] * num_blocks
    sizes = [len(block) for block in blocks]
    is_available = [
        indices[i] < sizes[i] for i in range(num_blocks)]
    num_unfinished = sum(is_available)
    result: list[int] = []

    while num_unfinished:
        min_index, min_key = -1, None
        for i in range(num_blocks):
            if is_available[i]:
                current_key = key_list[blocks[i][indices[i]]]
                if min_index < 0 or current_key < min_key: # type: ignore
                    min_index, min_key = i, current_key
        result.append(min_key) # type: ignore
        indices[min_index] += 1
        if indices[min_index] >= sizes[min_index]:
            is_available[min_index] = False
            num_unfinished -= 1
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
    size = len(items)
    group_size = max(1, int(sqrt(size)))
    steps = size // group_size
    sorted_blocks: list[list[int]] = []
    if key is None:
        key = lambda x: x
    key_list = [key(item) for item in items]
    for step in range(steps):
        start = step * group_size
        end = (step + 1) * group_size if step != steps - 1 else size
        sorted_blocks.append(
            __bubble_sort_values_by_keys(key_list[start:end], key_prefix=start))
    return [items[index] \
        for index in merge_sorted_lists(
            sorted_blocks, key_list)]