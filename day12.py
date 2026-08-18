def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def division(a,b):
    return(a/b)

num1=int(input("enter first number"))
num2=int(input("enter second number"))

answer=add(num1,num2)
print("answer" , answer)

answer=substract(num1,num2)
print("answer" , answer)

answer=multiply(num1,num2)
print("answer" , answer)

answer=division(num1,num2)
print("answer" , answer)