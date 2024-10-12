import random
while True:
    input("Press enter to start the game")
    result=random.randint(1,6)
    print("The die shows:",result)
    again=input("Roll again(y/n)?")
    if again=='n':
        break
