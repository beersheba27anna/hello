
import random

import functions
def __is_sorted(numbers: list[int])->str:
    lim: int = len(numbers) - 1
    i: int = 0
    while i < lim and numbers[i] <= numbers[i + 1]:
        i += 1
    return "sorted" if i >= lim else "unsorted"   
def __has_duplicates(numbers:list[int]) -> str:
    return "has duplicates" if len(numbers) > len(set(numbers)) else "doesn't have duplicates"
print(f"  max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]), expected: 100 ,\
actual: {functions.max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100])}")
print(f"  max_with_negative_duplicate([-100, 100, 20, 10, -10, 110, 1, 5, -30, -20, -110]), expected: 110 ,\
actual: {functions.max_with_negative_duplicate([-100, 100,20, 10, -10, 110, 1, 1, 5, -30, -20,  -110])}")
print(f" max_with_negative_duplicate([10, 20, -15, -11, 20]), expected: -1 ,\
actual: {functions.max_with_negative_duplicate([10, 20, -15, -11, 20])}")
print(f" max_with_negative_duplicate([10, 20, -15, -11, 20, 0, 0]), expected: -1 ,\
actual: {functions.max_with_negative_duplicate([10, 20, -15, -11, 20, 0, 0])}")
print(f"sumOfTwoExists([100, -10, 12, 12, -100], 24),\
 expected: True; actual: {functions.sumOfTwoExists([100, -10, 12, 12, -100], 24)}")
print(f"sumOfTwoExists([100, -10, 12, 12, -100], 0),\
 expected: True; actual: {functions.sumOfTwoExists([100, -10, 12, 12, -100], 0)}")
print(f"sumOfTwoExists([100, -10, 12, 12, -100], 25),\
 expected: False; actual: {functions.sumOfTwoExists([100, -10, 12, 12, -100], 25)}")
l_unsorted = [random.randint(1, 1000) for _ in range(1000)]
l_sorted = l_unsorted.copy()
functions.bubble_sort(l_sorted)
print(f"before sorting the list is {__is_sorted(l_unsorted)} after sorting the list is {__is_sorted(l_sorted)}")
l_dup = [random.randint(1, 10) for _ in range(100)]
l_no_dup = functions.remove_duplicates(l_dup)
print(f"before removing duplicates the list {__has_duplicates(l_dup)}\
 after removing duplicates the list {__has_duplicates(l_no_dup)}")