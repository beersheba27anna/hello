import functions

# print calls for testing the above functions
# indexOf
print(f"indexOf([10, 20, 30, 20, -1], 20). Expected value: 1; \
    actual value: {functions.indexOf([10, 20, 30, 20, -1], 20)}")
print('indexOf([10, 20, 30, 20, -1], 23)', '=>', functions.indexOf([10, 20, 30, 20, -1], 23))
print('indexOf([], 0)', '=>', functions.indexOf([], 0))

# lastIndexOf
print('lastIndexOf([10, 20, 30, 20, -1], 20)', '=>', functions.lastIndexOf([10, 20, 30, 20, -1], 20))
print('lastIndexOf([10, 20, 30, 20, -1], 23)', '=>', functions.lastIndexOf([10, 20, 30, 20, -1], 23))
print('lastIndexOf([], 20)', '=>', functions.lastIndexOf([], 20))

# min_even
print('min_even([-10001, 10, 20, 8, -7])', '=>', functions.min_even([-10001, 10, 20, 8, -7]))

# count
print('count([10, 20, 30, 20, -1], 20)', '=>', functions.count([10, 20, 30, 20, -1], 20))
print('count([10, 20, 30, 20, -1], 23)', '=>', functions.count([10, 20, 30, 20, -1], 23))
print('count([], 2)', '=>', functions.count([], 2))

# sumOfTwoExists
print('sumOfTwoExists([1, -1, 40, 50, 0], 0)', '=>', functions.sumOfTwoExists([1, -1, 40, 50, 0], 0))
print('sumOfTwoExists([1, -1, 40, 50, 0], 42)', '=>', functions.sumOfTwoExists([1, -1, 40, 50, 0], 42))