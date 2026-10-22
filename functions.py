def indexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its first occurrence,
        otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
        indexOf([10, 20, 30, 20, -1],23) => -1
    """
    i = 0
    size = len(numbers)
    while i < size and numbers[i] != num:
        i = i + 1
    return i if i < size else -1

def lastIndexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its last occurrence,
        otherwise -1. Examples: lastIndexOf([10, 20, 30, 20, -1],20) => 3,
        lastIndexOf([10, 20, 30, 20, -1],23) => -1
    """
    i = len(numbers) - 1
    while i >= 0 and numbers[i] != num:
        i = i - 1
    return i

def min_even (numbers):
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    example: min_even (-10001, 10, 20, 8, -7) => 8
    """ 
    result = -1 # default odd number
    for num in numbers:
        if num % 2 == 0 and (result == -1 or result > num):
            result = num
    return result 

def count(numbers, num) :
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
      Examples: count([10, 20, 30, 20, -1],20) => 2,
    count([10, 20, 30, 20, -1],23) => 0
    """
    return len([x for x in numbers if num==x])

def sumOfTwoExists(numbers, sum):
    """
    Optional task for advanced students
    To apply only the types discussed at the course up to now
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """ 
    result = False
    i = 0
    size = len(numbers)
    covered = []
    while not result and i < size:
        if numbers[i] in covered:
            result = True
        else:
            covered.append(sum - numbers[i])
        i = i + 1
    return result


# print calls for testing the above functions
# indexOf
print('indexOf([10, 20, 30, 20, -1], 20)', '=>', indexOf([10, 20, 30, 20, -1], 20))
print('indexOf([10, 20, 30, 20, -1], 23)', '=>', indexOf([10, 20, 30, 20, -1], 23))
print('indexOf([], 0)', '=>', indexOf([], 0))

# lastIndexOf
print('lastIndexOf([10, 20, 30, 20, -1], 20)', '=>', lastIndexOf([10, 20, 30, 20, -1], 20))
print('lastIndexOf([10, 20, 30, 20, -1], 23)', '=>', lastIndexOf([10, 20, 30, 20, -1], 23))
print('lastIndexOf([], 20)', '=>', lastIndexOf([], 20))

# min_even
print('min_even([-10001, 10, 20, 8, -7])', '=>', min_even([-10001, 10, 20, 8, -7]))

# count
print('count([10, 20, 30, 20, -1], 20)', '=>', count([10, 20, 30, 20, -1], 20))
print('count([10, 20, 30, 20, -1], 23)', '=>', count([10, 20, 30, 20, -1], 23))
print('count([], 2)', '=>', count([], 2))

# sumOfTwoExists
print('sumOfTwoExists([1, -1, 40, 50, 0], 0)', '=>', sumOfTwoExists([1, -1, 40, 50, 0], 0))
print('sumOfTwoExists([1, -1, 40, 50, 0], 42)', '=>', sumOfTwoExists([1, -1, 40, 50, 0], 42))