import time
print(time.strftime("%H:%M"))
alarm_time=input("enter alarm time(HH:MM):")
while time.strftime("%H:%M")!=alarm_time:
    time.sleep(1)
print("Time to wake up!")