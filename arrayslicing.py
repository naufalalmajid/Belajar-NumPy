# we can slicing array by [start:end] or if we using step become [start:end:step]
import numpy as np

arr = np.array([2, 8, 28, 555, 222, 888, 2222])
print(arr[1:])

# negative slicing, we can slicing by negative value which it is refer to index from the end
print(arr[-4:])

# we can use step value for determine the step of slicing
print(arr[::2])

# for slicing in 2-D arrays we can do
two = np.array([[2, 22, 28, 222, 2222], [8, 88, 555, 888, 8888]])
print(two[0:3, 3])
print(two[0, 1:3])
