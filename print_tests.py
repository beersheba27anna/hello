import hw_5

test_lists: list[list[int]] = [[], [1], [1, 2, 3], [3, -5 , 11, 2]]
min_max_avg_expected: list[tuple[int|None, int|None, float|None]] =\
    [(None, None, None), (1, 1, 1.0), (1, 3, 2.0), (-5, 12, 2.75)]

for ind, list_obj in enumerate(test_lists):
    print(f"minMaxAverage({list_obj}) =>\
        expected: {{{min_max_avg_expected[ind]}}}; actual: {{{hw_5.minMaxAverage(list_obj)}}}")

print("=========")

test_lists = [[], [1], [1, 2, 3], [3, -5 , 11, 2], [10, -1, 0]]
move_max_expected: list[list[int]] = [[], [1], [1, 2, 3], [3, -5 , 2, 11], [-1, 0, 10]]
original_input = []
for ind, list_obj in enumerate(test_lists):
    original_id = id(list_obj)
    original_input = list_obj.copy()
    hw_5.moveMaxToEnd(list_obj)
    new_id = id(list_obj)
    print(f"moveMaxToEnd({original_input}) =>\
        expected: {{{move_max_expected[ind]}}}; actual: {{{list_obj}}};\
        ids: original - {original_id} = new id - {new_id}")

