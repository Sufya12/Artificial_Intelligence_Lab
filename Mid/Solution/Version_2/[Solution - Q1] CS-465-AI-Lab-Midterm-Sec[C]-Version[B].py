# ask name and age                                              [POINTS: 2]

name = input("Enter your good name here: ")
age = int(input("Enter your age here: "))

# conditional statement                                         [POINTS: 3]

if age < 18:
    print("Dear {}, You're under age!".format(name))
else:
    print("Hey {}, You're eligible for vote casting.".format(name))