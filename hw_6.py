def max_with_negative_duplicate (numbers:list[int]) -> int:
    """
    Algorithm complexity should be O[N]
    numbers - list with integer numbers
    returns the maximal element of "numbers" with existing negative duplicate 
    (example of a number with negative duplicate: number 100, negative duplicate -100)
    If no such number exists, returns -1
    Examples: max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]) => 100
    max_with_negative_duplicate([10, 20, -15, -11, 20]) => -1
    """
    result = 0 # not interested in 0 value, so looking for large values
    reverse_numbers = set()
    for num in numbers:
        rev_num = -num
        abs_value = num if num >= 0 else rev_num
        if abs_value > result and num in reverse_numbers:
            result = abs_value
        reverse_numbers.add(rev_num)
    return result if result > 0 else -1 # has no negative

def sumOfTwoExists(numbers:list[int], sum: int) -> bool:
    """
    Algorithm complexity should be O[N]
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """
    remaining_values = set()
    result = False
    index = 0
    size = len(numbers)
    while not result and index < size:
        if numbers[index] in remaining_values:
            result = True
        else:
            remaining_values.add(sum-numbers[index])
        index += 1
    return result

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

def bubble_sort(numbers: list[int]) -> None:
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

def remove_duplicates(numbers: list[int]) -> list[int] :
    """
    Algorithm complexity O[N]
    returns new list containing all numbers from 'numbers' parameter
      except duplicates. The order should be kept
    Example:  'numbers' - [-1, 0, 100, -1, 20, 80, 20] the function should return
    new list [-1, 0, 100,  20, 80]
    """
    result = []
    unique_values = set()
    for num in numbers:
        if num not in unique_values:
            result.append(num)
            unique_values.add(num)
    return result