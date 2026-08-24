number = int(input("enter your number"))
if number==0:
    print("zero")
elif number>0:
    if number%2==0:
        print("positive even")
    else:
        print ("positive odd")
else:
    if number<0:
        if number%2==0:
            print("negative even")
        else:
            print("negative odd")