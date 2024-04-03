# with joining two or more arrays it is meaning make a new single array from it
# we can do it by using concatenate() function, along with axis
import numpy as np

arr1 = np.array([2, 8, 28, 88, 99, 222])
arr2 = np.array([555, 888, 2222, 5555, 8888, 9999])

newArr = np.concatenate((arr1, arr2))
print(newArr)

arr3 = np.array([[2, 5], [8, 9]])
arr4 = np.array([[22, 28], [88, 99]])

arr5 = np.concatenate((arr3, arr4), axis=1)
print(arr5)

# joining arrays using stack functions, stacking is same with concatenate, the difference is only stacking done along a new axis
arr6 = np.stack((arr1, arr2), axis=1)
print(arr6)

# stacking along rows by using hstack()
arr7 = np.hstack((arr3, arr4))
print(arr7)

# stacking along column by using vstack()
arr8 = np.vstack((arr3, arr4))
print(arr8)

# stacking along height (depth) by using dstack()
arr9 = np.dstack(arr3, arr4)
print(arr9)
