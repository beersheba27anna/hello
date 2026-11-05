import functions
# testing minMaxAverage
l1: list[int] = [10, 50, 20, 20]
min, max, avg = functions.minMaxAverage(l1)
print(f"minMaxAverage: list is {l1}, expected: min=10, max=50, avg=25.0;\
actual: min={min},max={max},avg={avg}")
#######################################################
# testing moveMaxToEnd
l2: list[int] = l1.copy()
functions.moveMaxToEnd(l2)
print(f"mooving the maximal to the end: list is {l1}, after moving: \
 expected last element is 50, actual is {l2[len(l1)-1]}")