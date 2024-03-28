# for make arrays in numpy called as ndarray, we can make it by using array function

import numpy as np

arr = np.array([2, 8, 28, 888, 2222, 888])
print(type(arr), arr)

# in arrays we have dimensions, which a dimensions in array is one lever of array depth (nested arrays)

# 0-D arrays
zero = np.array(28)
print(zero)

# 1-D arrays
one = np.array([2, 28, 222, 2222, 8888])
print(one)

# 2-D arrays, often used for represent matrix or 2nd
two = np.array([[2, 22], [8, 88]])
print(two)

# 3-D arrays
three = np.array([[[2, 22], [8, 88], [28, 88]]])
print(three)

# higher dimensional, we can define number of dimension by using ndmin argument
higher = np.array([2, 28, 888], ndmin=8)

# checking value number of dimension by using ndim
print(zero.ndim)
print(one.ndim)
print(two.ndim)
print(three.ndim)
print(higher.ndim)
