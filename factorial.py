#factorial
number=int(input("enter a number:"))
factorial=1;
if(number<0):
    print("Sorry,factorial won't exist for negative numbers")
elif(number==0):
    print("factorial of 0 is 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("The factorial of",number,"is",factorial)