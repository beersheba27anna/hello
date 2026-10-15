x = 0
while x < 5:
    print(x)
    x += 1

def exists(numbers, num):
    # numbers - list of integers
    # num - int number being tested for existence
    size, i = len(numbers), 0
    while i < size and numbers[i] != num:
        i += 1
    return i < size

numbers = [10, 20, 30]
print(exists(numbers, 15)) # False
print(exists(numbers, 30)) # True
