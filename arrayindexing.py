# like another indexing we can do same thing in arrray elements, with start from 0
import numpy as np

arr = np.array([2, 8, 222, 888])
print(arr[2])
print(arr[2] + arr[0])

# access 2-D arrays, first value is for dimension and second for index value
two = np.array([[2, 22], [8, 88]])
print(two[1, 1])

# access 3-D arrays, first value is for dimension, second for array element and third value for index value
three = np.array([[[2, 22], [8, 88]], [[28, 88], [222, 888]]])
print(three[1, 0, 1])

# negative indexing, access from the end
print(three[-1, -1, -2])
