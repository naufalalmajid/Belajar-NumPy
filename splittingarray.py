# spliting is reverse operation of joinings
# we can using array_splitting()
import numpy as np

arr = np.array([2, 8, 28, 88, 222, 555, 888, 22222])
arr1 = np.array_split(arr, 4)
print(arr1)

# in case less elements than needed it will automatic adjusted from the end accordingly
arr2 = np.array_split(arr, 5)
print(arr2)

# split into arrrays
arr3 = np.array_split(arr, 4)
print(arr3[0])
print(arr3[1])
print(arr3[2])
print(arr3[3])

# splitting 2-D arrays

