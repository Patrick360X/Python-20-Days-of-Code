import time

name = input("Enter you name: ")

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hrtime = int(time.strftime('%H'))
print(hrtime)


if(hrtime >= 0 and hrtime < 7):
    print("Hi", name, "Good Night, Sweet Dream")
elif(hrtime >= 7 and hrtime < 12):
    print("Hi", name, "Good Morning, Enjoy your day")
elif(hrtime >= 12 and hrtime < 17):
    print("Hi", name, "Good Afternoon and keep Working hard")
else:
    print("Hi", name, "Good Evening, what's up on the plans")