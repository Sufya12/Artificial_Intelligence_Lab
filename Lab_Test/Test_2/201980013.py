#QUESTION-01

tuple1=(99,99,99,99)

counte=0

for v in range (0,len(tuple1)):
    if tuple1[v] == 99:
        counte = counte+1
    else:
        print("All number not same ")
        
        
if counte==len(tuple1):
    print("All number are same")




####################################





import sys, random

s1={10,20,30,40,50}
s2={60,70,80,90,10}

if (s1 & s2):
    print(s1 & s2)
else:
    print("No common numbers")


class Dice:
    def init__(self):
        self.dice__value()
    def roll__dice(self):
        self.dice__value=random.randint(4,10)
        return self.dice__value

p1=Dice()
p2=Dice()
v1=p1.roll__dice()
v2=p2.roll__dice()    

if(v1>v2):
    print("player 1 win match ")
elif(v1<v2):
    print("player 2 win match ")
else:
    print("Draw match")

#QUESTION-02