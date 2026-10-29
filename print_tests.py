import functions
# print calls for testing the above functions
print(f"indexOf([10, 20, 30, 20, -1],20) expected value 1\
       actual value is {functions.indexOf([10, 20, 30, 20, -1],20)}") # should be 1
print(functions.indexOf([10, 20, 30, 20, -1], 23)) # should be -1
print(functions.lastIndexOf([10, 20, 30, 20, -1],20)) # should be 3
print(functions.lastIndexOf([10, 20, 30, 20, -1], 23)) # should be -1
print(functions.min_even ([-10001, 10, 20, 8, -7])) #should be 8
print(functions.count([10, 20, 30, 20, -1],20)) #should be 2
print(functions.count([10, 20, 30, 20, -1],23)) #should be 0
print(functions.sumOfTwoExists([1, -1, 40, 50, 0], 0)) #should be True
print(functions.sumOfTwoExists([1, -1, 40, 50, 0], 43)) #should be Frue