num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
operator=input("if operation is(+,-,*,/):")

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    if num2==0:
        print("cannot divide by zero")
    else:
        print(num1/num2)
    
else:
    print("invalid operator")