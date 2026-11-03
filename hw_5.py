def minMaxAverage(numbers: list[int]) -> tuple[int|None, int|None, float|None]:
    '''
    numbers - list with integer numbers
    returns minimum value, maximum value and average value of the numbers in the list numbers
    '''
    min_value: int|None = None
    max_value: int|None = None
    avg_value: float|None = None
    size = len(numbers)
    if size > 0:
        min_value, max_value, total =\
            numbers[0], numbers[0], numbers[0]
        for i in range(1, size):
            total += numbers[i]
            if numbers[i] < min_value:
                min_value = numbers[i]
            if numbers[i] > max_value:
                max_value = numbers[i]
        avg_value = total / size
    return min_value, max_value, avg_value

def moveMaxToEnd(numbers: list[int]) -> None:
    '''
    numbers - list with integer numbers
    moves maximum element of the list to the end
    no return value
    '''
    size = len(numbers)
    if size > 0:
        max_ind = 0
        for i in range(1, size):
            if numbers[max_ind] < numbers[i]:
                max_ind = i
        copy_value = numbers[max_ind]
        ind = size - 1
        while ind >= max_ind:
            numbers[ind], copy_value = copy_value, numbers[ind]
            ind -= 1