# import numpy package                                  [POINTS: 1]

import numpy as np

# create a matrix using Numpy built-in functions        [POINTS: 2]

matrix = np.arange(31, 47).reshape(4, 4)
print(matrix)

# get its order by shape method                         [POINTS: 1]

order = matrix.shape
print("order is {}".format(order))

# extract its mid by slicing                            [POINTS: 2]

mid = matrix[1:3, 1:3]
print(mid)