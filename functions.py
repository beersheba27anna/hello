from typing import Callable

def __move_end_by_length[T](
        items: list[T], start_seg1: int, start_seg2: int, move_size: int
        ) -> None:
    """
    moves segment of size move_size at starting start_seg2 at position
    start_seg1 while shifting segment of the same size from start_seg1
    forward
    """
    for shift in range(move_size):
        next_ind = start_seg2 + shift
        stored = items[next_ind]
        while next_ind > start_seg1 + shift:
            items[next_ind] = items[next_ind - 1]
            next_ind -= 1
        items[start_seg1 + shift] = stored

def merge_in_place[T](
        items: list[T], start: int, len1: int, size: int,
        key: Callable[[T], T]|None=None) -> None:
    """
    merges two sorted by key subparts in place of a list's part
    Time complexity O[N]
    Space complexity O[1] no additional list is created
    items - list of T objects (T any type generic at call time)
    start - start index of a being merged list
    len1 - length of the first subpart
    size - length of whole part
    Example: items - [3, 5, 7, -11, 0, 4, -10, -20, 100, -80,-4, 8 ], key - abs function
    start - 0; len1 - 4; size - 8
    call as  merge_in_place(items, start=0, len1=4, size=8, key=abs)
    updated itesms should be as [0, 3, 4, 5, 7, -10, -11, -20, 100, -80,-4, 8]
    """
    start1 = start
    start2 = start + len1

    end = start + size

    if key is None:
        key = lambda obj: obj

    while start1 < start2 < end:
        if key(items[start1]) > key(items[start2]):
            move_size = 0
            while start2 + move_size < end and\
                    key(items[start2 + move_size]) < key(items[start1]):
                move_size += 1
            __move_end_by_length(items, start1, start2, move_size)
            start1 += move_size
            start2 += move_size
        else:
            start1 += 1
