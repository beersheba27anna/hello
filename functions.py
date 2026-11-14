from typing import Callable, Sequence


def move_max_by_key_to_end(
        numbers: list[int], keys: list[object], stop: int) -> int:
    """
    - numbers - list with integer numbers
    - keys - corresponding to a specific value from numbers
    - stop - index where to stop sorting
    - moves maximum element (by corresponding key) of the list to the end ending from the index stop
    - returns int value index of minimum position affected by the last exchange
        returns -1 with no exchange hapenning
    """
    last_exchange_index = -1
    limit = len(numbers)-1 if stop >= len(numbers) else stop
    for index in range(limit):
        if keys[numbers[index]] > keys[numbers[index+1]]:
            numbers[index], numbers[index+1] =\
                numbers[index+1], numbers[index]
            last_exchange_index = index
    return last_exchange_index


def bubble_sort_values_by_keys(numbers: list[int], keys: list[object]) -> None:
    """
    Algorithm complexity is O[N^2]
    Write implementation of the bubble sorting algorithm
    Bubble sorting algorithm: sequentional pushing maximal numbers to the end
    Example: Initial list [100, 90, 80, 70] - worst case regarding total number of iterations
    1. Pushing 100 to the end of whole list, as a result there will be [90, 80, 70, 100] - 100 on its place at end
    2. Pushing 90 to the end of the part comprising of 3 ([90, 80, 70]) first elements, as a result there will be [ 80, 70, 90,100]
    3. Pushing 80 to the end of the part comprising of 2 ([80, 70]) first elements, as a result there will be [  70,80, 90,100]
    Totally 6 iterations: step 1 has 3 iterations, step 2 has 2 iterations ans step 3 has 1 iteration
    Common formula of the number of iterations for worst case is (n * (n - 1))/2
    """
    unsorted_end = len(numbers) - 1
    while unsorted_end > 0:
        unsorted_end = move_max_by_key_to_end(numbers, keys, unsorted_end)


def bubble_sorted(items: Sequence[object], key: Callable[[object], object]|None = None)->list[object]:
    """
    Sequence[object] means immutable list, so items cannot be updated
    returns new list of objects sorted using algorithm "bubble sort"
      in accorgance with key function-converter like standard Python sorting 
    items - sequence of any objects
    key - a function taking one object and returning converted object having standard operator ">"
          default value None designating standard Python sorting with no converting initial object
    For example, bubble_sort(numbers) - regular sort of numbers 
                 bubble_sort(numbers, abs) - sort of numbers in accordance with their abs values
    Unlike the standard sorting methods of Python, the function may be called with no explicit specifying key=                
    """
    key_values = [key(x) if key is not None else x for x in items]
    indices = list(range(len(items)))
    bubble_sort_values_by_keys(indices, key_values)
    return [items[x] for x in indices]


def even_asc_odd_desc(numbers: list[int])->list[int]:
    """
    returns new list of numbers sorted in the following order:
    The even numbers ordered by ascending order reside before odd numbers ordered by descending order
    For example, even_asc_odd_desc([-3, -10, 12, 3, -21, 6, 21, 5, 4 ]) returns [-10, 4, 6, 12, 21, 5, 3, -3, -21]
    """

def __extract_by_flatten_index(
        index: int, size_l1: int,
        parts: list[Sequence[object], Sequence[object]]):
    return parts[0][index] if index < size_l1 else parts[1][index - size_l1]

def  merge(part1: Sequence[object], part2: Sequence[object], key: Callable[[object], object]|None = None)->list[object]:
    """
    part1 and part2 -  sorted in accordance with key function-converter lists of any objects 
    key - a function taking one object and returning converted object having standard operator ">"
              default value None designating standard Python sorting with no converting initial objects
    returns new list, sorted in accordance with key function-converter, comprising of two lists-parts 
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4])  => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11 ], [ 0, 4, -10, -20 ], abs)  => [ 0, 3, 4, 5, 7, -10, -11,-20]
    """
    size_l1 = len(part1)
    size_l2 = len(part2)
    parts: list[Sequence[object]] = [part1, part2]
    indices = list(range(size_l1+size_l2))
    key_values = [key(__extract_by_flatten_index(
        ind, size_l1, parts))\
        if key is not None else __extract_by_flatten_index(
        ind, size_l1, parts)\
        for ind in indices]
    bubble_sort_values_by_keys(indices, key_values)
    return [__extract_by_flatten_index(
        ind, size_l1, parts) for ind in indices]