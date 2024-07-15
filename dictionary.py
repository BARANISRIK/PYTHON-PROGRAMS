keys=[]
values=[]
n=int(input("enter the number of elements:"))
print("For keys")
for i in range(0,n):
    element=int(input("enter the key:"))
    keys.append(element)
print("For values:")
for i in range(0,n):
    element=input("enter the value:")
    values.append(element)
d=dict(zip(keys,values))
print("Dictionary elements:",d)