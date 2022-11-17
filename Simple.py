dogBreeds = ["Great Pyrenees", "Australian Shepherd" ,"Golden Retriever","Bulldog"]
input = input("Which dog breed do you want: ")

#Getting every item in dogBreeds checking the input and looking for the same "Name" in the list
for i in dogBreeds:
    if input == i:
        print("We Found the dog!!!")
    else:
        print("Dog not found")
    break

