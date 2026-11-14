from typing import Callable, Sequence


def move_max_to_end(numbers: list[int], stop: int) -> None:
    '''
    numbers - list with integer numbers
    stop - index where to stop sorting
    moves maximum element of the list to the end endign from the index stop
    no return value
    '''
    limit = len(numbers)-1 if stop >= len(numbers) else stop
    for index in range(limit):
        if numbers[index] > numbers[index+1]:
            numbers[index], numbers[index+1] =\
                numbers[index+1], numbers[index]

def bubble_sort_old(numbers: list[int]) -> None:
    """
    Algorithm complexity is O[N^2]
    Write implementation of the bubble sorting algorithm
    Bubble sorting algorithm: sequentional pushing maximal numbers to the end
    Example: Initial list [100, 90, 80, 70] - worst case regarding total number of iterations
    1. Pushing 100 to the end of whole list, as a result there will be [90, 80, 70, 100] - 100 on its place at end
    2. Pushing 90 to the end of the part comprising of 3 ([90, 80, 70]) first elements, as a result there will be [ 80, 70, 90,100]
    3. Pushing 80 to the end of the part comprising of 2 ([80, 70]) first elements, as a result there will be [  70,80, 90,100]
    Totally 6 iterations: step 1 has 3 iterations, step 2 has 2 iterations ans step 4 has 1 iteratiion
    Common formula of the number of iterations for worst case is (n * (n - 1))/2
    """
    for ind in range(len(numbers) - 1, 0, -1):
        move_max_to_end(numbers, ind)

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

def even_asc_odd_desc(numbers: list[int])->list[int]:
    """
    returns new list of numbers sorted in the following order:
    The even numbers ordered by ascending order reside before odd numbers ordered by descending order
    For example, even_asc_odd_desc([-3, -10, 12, 3, -21, 6, 21, 5, 4 ]) returns [-10, 4, 6, 12, 21, 5, 3, -3, -21]
    """

def  merge(part1: Sequence[object], part2: Sequence[object], key: Callable[[object], object]|None = None)->list[object]:
    """
    part1 and part2 -  sorted in accordance with key function-converter lists of any objects 
    key - a function taking one object and returning converted object having standard operator ">"
              default value None designating standard Python sorting with no converting initial objects
    returns new list, sorted in accordance with key function-converter, comprising of two lists-parts 
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4])  => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11 ], [ 0, 4, -10, -20 ], abs)  => [ 0, 3, 4, 5, 7, -10, -11,-20]
    """
