from list import *

#PROBLEM #1 | i want to get all class items without creating a list first
allDogs = [dog1,dog2,dog3,dog4]

#checking input value
while True:
    try:
        print("--------------------------------")
        inputName = str(input("DogName: "))
        inputAge = int(input("Dog Age: "))
        print("--------------------------------")
    except ValueError:
        print("Invalid input.")
        continue
    else:
        break

for i in allDogs:
    if (inputAge == i.age) and (inputName == i.name):
        print(i)
        break
    else:
            break