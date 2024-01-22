# INSTRUCTIONS

# Class Participation 03

# 1. File name should be "Your_ID.py" e.g "18802585.py".
# 2. You don't need to create a new file. Edit this file and add your answer.
# 3. Finally, submit this file with your answers.
# 4. If you've any additional files like "story.txt" / "student.csv", don't submit them.
# 5. Only SUBMIT this "Your_ID.py" file with your answers.
# 6. Don't edit or remove any line or comment.


# Exercise-01
# Create an array of table 02 unig Numpy Array and then Iterate it.
# 
# 
# write your answer here... .. .


#Task 01

import numpy as np
y = np.array([[100, 200, 300, 400], [500, 600, 700, 800], [900, 1000, 1100, 1200]])
print(y)




# 
# Exercise-02
# Create 8-by-8 matrix and fill it with a pattern of checkerboard like
# 0 1 0
# 1 0 1
# 0 1 0
# 
# 
# write your answer here... .. .
# 
#



 
#Task2

import numpy as np
ya = np.ones((3,3))

print(" pattern of Checkerboard:")
ya = np.zeros((8,8),dtype=int)
ya[1::2,::2] = 1
ya[::2,1::2] = 1
print(ya)




# Exercise-03
# Create 10-by-10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
# 
# 
# write your answer here... .. .
# 



#Task 3

import numpy as np
ya = np.ones((10, 10))
ya[1:-1, 1:-1] = 0
print(ya)




# Exercise-04
# Create a given matrix first then find the number of rows and columns.
# [[10 11 12 13]
# [14 15 16 17]
# [18 19 20 21]]
# 
# 
# write your answer here... .. .
# 
#Task 04


import numpy as np
ya = np.array([[10,11,12,13],[14,15,16,17],[18,19,20,21]])
print(ya.shape)
 

# Exercise-05
# Reshape above 2-D array to one dimensional array
# 
# 
# write your answer here... .. .
# 
 

#Task 05


import numpy as np
ya = np.array([[100,110,120,103],[104,105,106,107],[108,109,200,210]])

re_ya = np.ravel(ya)
print("reshape 1d array =")
print(re_ya)

# Exercise-06
# Create a 5-by-7 matrix filled with values from 55 to 90
# 
# 
# write your answer here... .. .
# 
# 


#Task 06


import numpy as np
ya = np.arange(55,90).reshape((5,7))
print(ya)

########################END########################