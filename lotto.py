import random

def exists(numbers, num):
    """
    # numbers list of integers
    # num - being tested number for existence
    returns True if "num" exists in list "numbers" otherwise False
    """
    matching_numbers = [n for n in numbers if n == num]
    return len(matching_numbers) > 0

def generate_and_check(numbers, i, min, max):
    new_number = random.randint(min, max)
    numbers[i] = new_number if not exists(numbers, new_number)\
        else generate_and_check(numbers, i, min, max)
    return numbers[i]
    
def distinct_random_numbers(min, max, size):
    """
    
    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """

    result = []
    #integer numbers are assumed
    if max - min + 1 >= size:
        # populate with default
        result = [min-1 for _ in range(size)]
        result = [generate_and_check(result, i, min, max) for i in range(size)]
    return result

print (distinct_random_numbers(1, 49, 7))