import random
list=[]
num=int(input("enter the number of elements:"))
for i in range(num):
   list.append(random.randint(1,20)) 
print('random numbers:',list)