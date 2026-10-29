text: str = "Hello world!"
a: int = 10
text += str(10)
def add(op1:int, op2:int)->int:
    return op1 + op2
# string interpolation
text_f:str = f"Result of adding {2} and {{3}} is {{{add(3, 2)}}}."
print(text_f)