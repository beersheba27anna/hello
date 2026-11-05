# see README.md for HW# 5 definition
def minMaxAverage(numbers: list[int])->tuple[int, int, float]:
    min: int = numbers[0]
    max: int = numbers[0]
    total: int = 0
    for num in numbers:
        if num < min:
            min = num
        elif num > max:
            max = num
        total += num
    return min, max, total / len(numbers)  
 
def  moveMaxToEnd(numbers: list[int]) :
    for i in range(len(numbers) - 1) :
        if numbers[i] > numbers[i + 1] :
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]