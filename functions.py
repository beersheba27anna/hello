from typing import Callable, Sequence


def __move_max_by_key_to_end(
        indices: list[int], keys: list[object], stop: int) -> int:
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
        if keys[indices[index]] > keys[indices[index+1]]:  # pyright: ignore[reportOperatorIssue]
            indices[index], indices[index+1] = indices[index+1], indices[index]
            last_exchange_index = index
    return last_exchange_index


def __bubble_sort_values_by_keys(keys: list[object]) -> list[int]:
    """
    Bubble sort algorithm returning indices of the elements
    to sort the keys in ascending order
    """
    indices = list(range(len(keys)))
    unsorted_end = len(keys) - 1
    while unsorted_end > 0:
        unsorted_end = __move_max_by_key_to_end(indices, keys, unsorted_end)
    return indices

def __extract_key_or_default(
        items: Sequence[object],
        key: Callable[[object], object] | None = None) -> list[object]:
    return list(items) if key is None else [key(item) for item in items]


def bubble_sorted(items: Sequence[object], key: Callable[[object], object] | None = None) -> list[object]:
    """
    Sequence[object] means immutable list, so items cannot be updated
    returns new list of objects sorted using algorithm "bubble sort"
      in accordance with key function-converter like standard Python sorting 
    items - sequence of any objects
    key - a function taking one object and returning converted object having standard operator ">"
          default value None designating standard Python sorting with no converting initial object
    For example, bubble_sort(numbers) - regular sort of numbers 
                 bubble_sort(numbers, abs) - sort of numbers in accordance with their abs values
    Unlike the standard sorting methods of Python, the function may be called with no explicit specifying key=                
    """
    key_values = __extract_key_or_default(items, key=key)
    indices = __bubble_sort_values_by_keys(key_values)
    return [items[ind] for ind in indices]


def even_asc_odd_desc(numbers: list[int]) -> list[int]:
    """
    returns new list of numbers sorted in the following order:
    The even numbers ordered by ascending order reside before odd numbers ordered by descending order
    For example, even_asc_odd_desc([-3, -10, 12, 3, -21, 6, 21, 5, 4 ]) returns [-10, 4, 6, 12, 21, 5, 3, -3, -21]
    """
    return bubble_sorted(  # pyright: ignore[reportReturnType]
        numbers,
        key=lambda num: (0, num) if num % 2 == 0 else (1, -num))  # pyright: ignore[reportOperatorIssue, reportUnknownLambdaType]


def merge(part1: Sequence[object], part2: Sequence[object], key: Callable[[object], object] | None = None) -> list[object]:
    """
    part1 and part2 - sorted in accordance with key function-converter lists of any objects 
    key - a function taking one object and returning converted object having standard operator ">"
            default value None designating standard Python sorting with no converting initial objects
    returns new list, sorted in accordance with key function-converter, comprising of two lists-parts 
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4])  => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11 ], [ 0, 4, -10, -20 ], abs)  => [ 0, 3, 4, 5, 7, -10, -11,-20]
    """

    ind1, ind2 = 0, 0
    size1 = len(part1)
    size2 = len(part2)

    result: list[object] = []

    part1_keys = __extract_key_or_default(part1, key=key)
    part2_keys = __extract_key_or_default(part2, key=key)
    while ind1 < size1 or ind2 < size2:
        if ind2 >= size2 or (
                ind1 < size1 and not (part1_keys[ind1] > part2_keys[ind2])):  # pyright: ignore[reportOperatorIssue]
            result.append(part1[ind1])
            ind1 += 1
        else:
            result.append(part2[ind2])
            ind2 += 1
    return result