#armstrong
Number=int(input("Enter a number:"))
length=len(str(Number))
sum=0
temp=Number;
while temp>0:
    digit=temp%10
    sum+=digit**length
    temp=temp//10
print("the number is {} and sum is {}".format(Number,sum))
if(Number==sum):
    print("Armstrong number")
else:
    print("Not an armstrong number")
