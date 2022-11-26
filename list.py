#Creating Class dog for ease of creating dogs
class Dog:
    
    #Creating constructor and Objects
    def __init__(self,breed,name,age,pickup):
        self.breed = breed
        self.name = name
        self.age = age
        self.pickup = pickup
         
    #Checking if the dog is ready for Pickup
        if self.pickup == True:
            self.pickup = self.name + " is ready for pickup"
        elif self.pickup == False:
            self.pickup =  self.name + " is not ready for pickup"
        else:
            self.pickup = "ERROR"

    def __str__(self):
        return f'-------------- Dog {self.name} --------------\n Breed|{self.breed}\n Name|{self.name}\n Age|{self.age}\n Status|{self.pickup} \n---------------------------------------'

#list of dogs
dog1 = Dog("Australian Shepherd","Clair",5,True)
dog2 = Dog("Shiba Inu","Ubuntu",2,False)
dog3 = Dog("Great Pyrenees","Bond",4,True)
dog4 = Dog("Golden Retriever","Micheal",8,False)