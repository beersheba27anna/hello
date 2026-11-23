from typing import Callable
from random import randint, choice

from unittest_print import print_test, print_results
from functions import get_all_range, get_all_not_in_range
from functions import my_sorted

num_of_test = 100
size_limit = 10
possible_keys: list[Callable[[int], int]| None] =\
    [None, abs, lambda x: x % 21]
for _ in range(num_of_test):
    size = randint(a=0, b=size_limit*2)
    test_list_in = sorted([randint(-size_limit*10, size_limit*10) for x in range(size)])
    min_value = randint(-size_limit, size_limit)
    max_value = randint(-size_limit, size_limit)
    step = randint(-5, 5)
    step = step if step != 0 else 1
    range_in = range(min_value, max_value, step)
    expected_out_in = []
    if len(range_in) > 0:
        max_range, min_range = max(range_in), min(range_in)
        expected_out_in = [
            num for num in test_list_in\
                if min_range <= num <= max_range]
    expected_out_out = [num for num in test_list_in if num not in range_in]
    print_test(f'Numbers from list {test_list_in} in range {range_in}',
        expected_out_in, get_all_range(test_list_in, range_in))
    print_test(f'Numbers from list {test_list_in} not in range {range_in}',
        expected_out_out, get_all_not_in_range(test_list_in, range_in))
    current_key_func = choice(possible_keys)
    print_test(f"Sorted version of list {test_list_in}",
        sorted(test_list_in, key=current_key_func),
        my_sorted(test_list_in, key=current_key_func))
print_results()