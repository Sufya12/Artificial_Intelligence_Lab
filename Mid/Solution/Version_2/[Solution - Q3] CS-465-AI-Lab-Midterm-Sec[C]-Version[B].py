# *******************************************
# * FALL 2021 - Artificial Intelligence Lab *
# * MIDTERM PRACTICAL EXAM                  *
# *                                         *
# *******************************************
# *										    *
# * Car.py implementation: 10               *
# *								            *
# *******************************************
# *                                         *
# * ID:                                     *
# * NAME:                                   *
# * SECTION:                                *
# *                                         *
# * INSTRUCTIONS:                           *
# * Complete the implementation of the      *
# * following code, indicated in comments.  *
# *******************************************

class Car:
    
    # Complete the initializer with three private members
    # named as year_model, make, speed                          [POINTS: 1]

    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # write getters for all three members                       [POINTS: 1]

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    # write setters for all three members                       [POINTS: 1]

    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed

    # Complete implementation of str method with appropriate
    # message                                                   [POINTS: 1]

    def __str__(self):
        return "Car: [Year model = {}, Make = {}, Speed = {}]".format(self.get_year_model(), self.get_make(), self.get_speed())

# **************************************************************************
#
# Object Creation:
#
# Create three objects of above class with relevant information
# below this line                                               [POINTS: 2]

obj1 = Car(1990, "Audi", 800)
obj2 = Car(2006, "Honda", 1200)
obj3 = Car(2002, "Mehran", 600)

# Create a list and add above three objects to the list         [POINTS: 2]

list = [obj1, obj2, obj3]

# write a loop to iterate through list and display all objects  [POINTS: 2]

for i in list:
    print(i)

# **************************************************************************
# *                              END OF FILE                               *
# **************************************************************************