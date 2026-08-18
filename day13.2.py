def add (a , b):
    return a + b
def substract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))

answer=add(num1,num2)
print("addition=",answer)
answer=substract(num1,num2)
print("substraction=",answer)
answer=divide(num1,num2)
print("divide=",answer)
answer=multiply(num1,num2)
print("multiply=",answer)