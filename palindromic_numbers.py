def int_reverse(num):
    """
    returns string containing digits  of integer number "num" in reversed order
    if "num" contains only one digit it will return the same digit but as a string
    examples: int_reverse(10) -> "01"; int_reverse(1) -> "1";int_reverse(702) -> "207"
    """
    return str(num)[::-1]


def create_palindromic_list(start, stop) :
    """
    start, stop are integer numbers
    returns list containing all palindromic numbers in the range from "start" to "stop" 
    note: "start" may be less than "stop"
    requirement: to use "int_reverse" function
    """
    step = -1 if start > stop else 1
    
    # negative numbers never palindromes
    # stop is not included so need -1 to have 0
    stop = stop if stop >= 0 else -1
    start = start if start >= 0 else -1
    start = 0 if step == 1 and start == -1 else start 

    result = [num for num in range(start, stop, step)
        if str(num) == int_reverse(num)]
    return result

print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22]