################
# Author: Andrew Wang
# Date: 12/01/2019
# This programs stimulates a car accelerate and break with increasing and decreaing speed
#################
#Creates the class Car
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        
    def accerlate(self):
        self.__speed += 5
        return self.__speed

    def brake(self):
        self.__speed -= 5
        return self.__speed

    def get_speed(self):
        return self.__speed

#Main function 
def main():
    car = Car(0,0)
    print('Car is accelerating:')
    for i in range(5):
        car.accerlate()
        print('Current speed:',car.get_speed())

    print('\nCar is braking:')
    for i in range(5):
        car.brake()
        print('Current speed:', car.get_speed())

#Calls main function
main()
