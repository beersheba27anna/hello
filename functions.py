def indexOf(numbers:list[int], num:int)->int:
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its first occurrence,
        otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
        indexOf([10, 20, 30, 20, -1],23) => -1
    """
    i:int = 0
    size:int = len(numbers)
    while i < size and numbers[i] != num:
        i = i + 1
    return i if i < size else -1

def lastIndexOf(numbers:list[int], num:int)->int:
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its last occurrence,
        otherwise -1. Examples: lastIndexOf([10, 20, 30, 20, -1],20) => 3,
        lastIndexOf([10, 20, 30, 20, -1],23) => -1
    """
    i:int = len(numbers) - 1
    while i >= 0 and numbers[i] != num:
        i = i - 1
    return i

def min_even (numbers:list[int])->int:
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    example: min_even (-10001, 10, 20, 8, -7) => 8
    """ 
    result:int = -1 # default odd number
    for num in numbers:
        if num % 2 == 0 and (result == -1 or result > num):
            result = num
    return result

def count(numbers:list[int], num:int)->int:
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
      Examples: count([10, 20, 30, 20, -1],20) => 2,
    count([10, 20, 30, 20, -1],23) => 0
    """
    result = 0
    for x in numbers:
        if num == x:
            result = result + 1
    return result

def sumOfTwoExists(numbers:list[int], sum:int)->bool:
    """
    Optional task for advanced students
    To apply only the types discussed at the course up to now
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """ 
    result:bool = False
    i:int = 0
    size:int = len(numbers)
    covered:list[int] = []
    while not result and i < size:
        if numbers[i] in covered:
            result = True
        else:
            covered.append(sum - numbers[i])
        i = i + 1
    return result
