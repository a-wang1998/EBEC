################
# Author: Andrew Wang
# Date: 12/01/2019
# This programs allows user to input information of their pet and prints it out using class
#################
#Creates the class Pet
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name
        return self.__name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        return self.__animal_type

    def set_age(self, age):
        self.__age = age
        return self.__age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
        
#Main function 
def main():
    #Allows user to input information of the pet
    name = input(str('Enter the name of the pet: '))
    animal_type = input(str('Enter the type of animal: '))
    age = input(str('Enter the age of the pet: '))

    pet = Pet(name, animal_type, age)
    print('\nHere is the data that you entered:')
    print('Pet name:', pet.get_name())
    print('Animal type:', pet.get_animal_type())
    print('Age of pet:', pet.get_age())

#Calling main function
main()
