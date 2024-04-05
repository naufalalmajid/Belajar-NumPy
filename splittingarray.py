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
arr4 = np.array([[2, 8], [28, 99], [222, 555], [2222, 8888]])
arr5 = np.array_split(arr4, 2)
print(arr5)

arr6 = np.array_split(arr4, 2, axis=1)
print(arr6)

# alternate using hsplit() opposite of hstack()
arr7 = np.hsplit(arr4, 2)
print(arr7)
