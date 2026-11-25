from typing import Callable, Sequence
from typing import cast

def __merge_second_list[T, K](
        items: Sequence[T], added_block: Sequence[T],\
        key: Callable[[T], T|K])->list[T]:
    temp: list[T] = []
    i1 = 0; i2 = 0
    size1 = len(items); size2 = len(added_block)
    while i1 < size1 and i2 < size2:
        if key(items[i1]) <= key(added_block[i2]): # pyright: ignore[reportOperatorIssue]
            temp.append(items[i1])
            i1 += 1
        else:
            temp.append(added_block[i2])
            i2 += 1
    temp.extend(items[i1:size1])
    temp.extend(added_block[i2:size2])
    return temp


def my_sorted[T, K](items: Sequence[T],/,*, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    1. Creating list of already sorted by key parts from "items"
      (no additional sorting is required)
    2. Merge of all parts from the created above list
    """
    if key is None:
        key = lambda item: item
    start_index = 0; size = len(items)
    sorted_blocks: list[list[T]] = []
    for end_index in range(size-1):
        if key(items[end_index]) > key(items[end_index+1]):  # type: ignore
            sorted_blocks.append(cast(list[T], items[start_index:end_index+1]))
            start_index = end_index + 1
    sorted_blocks.append(cast(list[T], items[start_index:]))

    while len(sorted_blocks) > 1:
        current_size = len(sorted_blocks)
        sorted_until = current_size // 2
        for i in range(sorted_until):
            sorted_blocks[i] = \
                __merge_second_list(
                    sorted_blocks[2*i], sorted_blocks[2*i+1], key=key)
        if current_size % 2 != 0:
            sorted_blocks[sorted_until] = sorted_blocks[-1]
            sorted_until += 1
        del sorted_blocks[sorted_until:]
    return sorted_blocks[0]