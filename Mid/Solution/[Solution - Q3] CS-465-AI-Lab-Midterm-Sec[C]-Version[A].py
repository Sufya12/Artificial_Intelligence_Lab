# *******************************************
# * FALL 2021 - Artificial Intelligence Lab *
# * MIDTERM PRACTICAL EXAM                  *
# *                                         *
# *******************************************
# *										    *
# * Employee.py implementation: 10          *
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

class Employee:

    # Complete the initializer with three private members
    # named as name, dept, designation                          [POINTS: 1]

    def __init__(self, name, dept, designation):
        self.__name = name
        self.__dept = dept
        self.__designation = designation

    # write getters for all three members                       [POINTS: 1]

    def get_name(self):
        return self.__name

    def get_dept(self):
        return self.__dept

    def get_designation(self):
        return self.__designation

    # write setters for all three members                       [POINTS: 1]

    def set_name(self, name):
        self.__name = name

    def set_dept(self, dept):
        self.__dept = dept

    def set_designation(self, designation):
        self.__designation = designation

    # Complete implementation of str method with appropriate
    # message                                                   [POINTS: 1]

    def __str__(self):
        return "Employee: [Name = {}, Department = {}, Designation = {}]".format(self.get_name(), self.get_dept(), self.get_designation())


# **************************************************************************
#
# Object Creation:
#
# Create three objects of above class with relevant information
# below this line                                               [POINTS: 2]

obj1 = Employee("Addison", "Administrator", "CEO")
obj2 = Employee("John", "IT", "Operator")
obj3 = Employee("Abigale", "HR", "Hiring Manager")
# Create a list and add above three objects to the list         [POINTS: 2]

list = [obj1, obj2, obj3]

# write a loop to iterate through list and display all objects  [POINTS: 2]

for i in list:
    print(i)

# **************************************************************************
# *                              END OF FILE                               *
# **************************************************************************