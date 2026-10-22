numbers = [100, 7, 22, -6]
exists = 10 in numbers
print(exists, type(exists))

def exists(numbers, num):
    return num in numbers

print(exists(numbers, 10))