# copy and view in numpy have many difference, the main difference is copy is a new array and view is just view the original array
import numpy as np

arr = np.array([2, 8, 28, 555, 222, 888, 2222])
newArr = arr.copy()
arr[4] = 555
print(arr)
print(newArr)

viewArr = arr.view()
print(arr)
print(viewArr)

# check if array owns its data, we can use base attribute for checking and will be result None if copy
print(newArr.base)
print(viewArr.base)
