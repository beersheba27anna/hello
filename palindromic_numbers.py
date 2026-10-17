def int_reverse(num):
    """
    returns string containing digits  of integer number "num" in reversed order
    if "num" contains only one digit it will return the same digit but as a string
    examples: int_reverse(10) -> "01"; int_reverse(1) -> "1";int_reverse(702) -> "207"
    """
    sign = ""
    if num < 0:
        sign = "-"
        num = -1*num
    result = ""
    while num >= 10:
        result += str(num % 10)
        num = num // 10
    result += str(num)
    result += sign
    return result

def create_palindromic_list(start, stop) :
    """
    start, stop are integer numbers
    returns list containing all palindromic numbers in the range from "start" to "stop" 
    note: "start" may be less than "stop"
    requirement: to use "int_reverse" function
    """
    result = []
    step = -1 if start > stop else 1
    for num in range(start, stop, step):
        if str(num) == int_reverse(num):
            result.append(num)
    return result

print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22]
