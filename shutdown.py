import os
check=input("want to shutdown the computer?(y/n):")
if check=='n':
    exit();
else:
    os.system("shutdown/s/t1")
check=input("want to restart your computer?(y/n):")
if check=='n':
    exit();
else:
    os.system("shutdown/r/t1")