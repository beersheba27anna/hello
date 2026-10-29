a: int = 0
if a: # 10 considered as True
    print(True)

l:list[int] = [1, 2, 3]
if l:
    print(True)
if 0.0: # 0, 0.0 considered as False
    print(True)
else:
    print(False)
print(bool(l))
# "False" => True
# "" => False
# " " => True
# [] => False
if " ": print("space is True")
n: None = None
if n is None: print("none")
if n:
    print("n containing None is True")
else:
    print("n containing None is False")
# a = None vs code error since None is another type