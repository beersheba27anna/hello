import hw_6

test_in_min_max: list[list[int]] = [
    [-100, 20, 10, -10, 1, 1, 5, -30, -20, 100], [10, 20, -15, -11, 20]]
max_with_negative_duplicate_expected: list[int] =\
    [100, -1]

for ind, in_obj in enumerate(test_in_min_max):
    print(f"max_with_negative_duplicate({in_obj}) =>\
        expected: {{{max_with_negative_duplicate_expected[ind]}}}; actual: {{{hw_6.max_with_negative_duplicate(in_obj)}}}")

print("=========")

test_in_sumOfTwoExists: list[tuple[list[int], int]] =\
    [([1, -1, 40, 50, 0], 0), ([1, -1, 40, 50, 0], 42)]
sumOfTwoExists_expected:list[bool] =\
    [True, False]
for ind, in_obj in enumerate(test_in_sumOfTwoExists):
    print(f"sumOfTwoExists({in_obj}) =>\
        expected: {{{sumOfTwoExists_expected[ind]}}}; actual: {{{hw_6.sumOfTwoExists(*in_obj)}}}")

print("=========")

test_in_bubble_sort: list[int] =\
    [[100, 90, 80, 70], [1, 2, 3], [3, 2, 1, 8, 2, 4]]
bubble_sort_expected:list[bool] =\
    [[70, 80, 90, 100], [1, 2, 3], [1, 2, 2, 3, 4, 8]]
for ind, in_obj in enumerate(test_in_bubble_sort):
    print(f"bubble_sort({in_obj}) =>\
        expected: {{{bubble_sort_expected[ind]}}}; actual: {{{hw_6.bubble_sort(in_obj)}}}")

print("=========")

test_in_remove_duplicates: list[int] =\
    [[-1, 0, 100, -1, 20, 80, 20], [1, 2, 3], [3, 2, 1, 8, 2, 4]]
remove_duplicates_expected:list[bool] =\
    [[-1, 0, 100,  20, 80], [1, 2, 3], [1, 2, 3, 4, 8]]
for ind, in_obj in enumerate(test_in_remove_duplicates):
    print(f"remove_duplicates({in_obj}) =>\
        expected: {{{bubble_sort_expected[ind]}}}; actual: {{{hw_6.remove_duplicates(in_obj)}}}")

print("=========")