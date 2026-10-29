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
        i += 1
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
        i -= 1
    return i    
def min_even (numbers):
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    example: min_even ([-10001, 10, 20, 8, -7]) => 8
    """ 
    res = 1
    for num in numbers:
        if num % 2 == 0 and (res == 1 or num < res):
            res = num
    return res        
def count(numbers, num) :
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
      Examples: count([10, 20, 30, 20, -1],20) => 2,
    count([10, 20, 30, 20, -1],23) => 0
    """
    result = 0
    for number in numbers:
        if number == num:
            result += 1
    return result        
def sumOfTwoExists(numbers, sum):
    """
    Optional task for advanced students
    To apply only the types discussed at the course up to now
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """ 
    # additional helper function __existsFromIndex defined below
    i = 0
    limit = len(numbers) - 1 # last index should be length - 2
    while i < limit and not  __existsFromIndex(i + 1, numbers, sum - numbers[i]):
        i += 1
    return i < limit    

def  __existsFromIndex(start, numbers, num):
    size = len(numbers) 
    while start < size and numbers[start] != num:
        start += 1
    return start < size


# print calls for testing the above functions
print(indexOf([10, 20, 30, 20, -1],20)) # should be 1
print(indexOf([10, 20, 30, 20, -1], 23)) # should be -1
print(lastIndexOf([10, 20, 30, 20, -1],20)) # should be 3
print(lastIndexOf([10, 20, 30, 20, -1], 23)) # should be -1
print(min_even ([-10001, 10, 20, 8, -7])) #should be 8
print(count([10, 20, 30, 20, -1],20)) #should be 2
print(count([10, 20, 30, 20, -1],23)) #should be 0
print(sumOfTwoExists([1, -1, 40, 50, 0], 0)) #should be True
print(sumOfTwoExists([1, -1, 40, 50, 0], 43)) #should be Frue







