import os
import sys
from list import *

#PROBLEM #1 | i want to get all class items without creating a list first
allDogs = [dog1,dog2,dog3,dog4]

#checking input value
while True:
    try:
        print("\n--------------------------------")
        inputName = str(input("DogName: "))
        inputAge = int(input("Dog Age: "))
    except ValueError:
        print("--------------------------------")
        print("Invalid input.")
        continue
    else:
        break

for i in allDogs:
    if (inputName == i.name and inputAge == i.age):
        print(i)
        break
else:
    print("--------------------------------")
    retry = input("Dog not found  Try again? y/n: ").lower()
    if retry == "y":
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif retry == "n":
        print("Goodbye")
    else:
        print("ERROR")