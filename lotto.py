import random

def exists(numbers, num):
    """
    returns True if "num" exists in list "numbers" otherwise False
    """
    for element in numbers:
        if isinstance(element, int) and num == element:
            return True
    return False

def distinct_random_numbers(min, max, size):
    """
    
    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """

    result = []

    #integer numbers are assumed
    if max - min + 1 < size:
        return result
    while len(result) < size:
        new_number = random.randint(min, max)
        if not exists(result, new_number):
            result.append(new_number)
    return result

print (distinct_random_numbers(1, 49, 7))