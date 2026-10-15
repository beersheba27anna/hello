s = "abc"
d = 2
# error: print(s + 2)
print (s + str(d))
# runtime error, impossible to convert - print(int(s) + d)