# iterating means going through elements on by one
# we can do it be using for loop
import numpy as np

arr = np.array([2, 8, 28, 88, 99, 222, 555, 888, 999, 2222, 5555, 8888, 9999])

for x in arr:
    print(x)

# iterating 2-D arrays
arr2 = np.array([[2, 28, 99], [222, 555, 2222]])
for y in arr2:
    print(y)
# iterating the arrays in each dimension
for z in arr2:
    for xyz in z:
        print(xyz)

# iterating 3-D arrays
arr3 = np.array([[[2, 8, 9], [22, 28, 99]], [[222, 555, 888], [2222, 5555, 8888]]])
for yz in arr3:
    print(yz)

for a in arr3:
    for b in a:
        for c in b:
            print(c)

# iterating using nditer attribute
for yzx in np.nditer(arr3):
    print(yzx)

# iterating with different data type
for yx in np.nditer(arr, flags=["buffered"], op_dtypes="S"):
    print(yx)

# iterating with different step size
for xy in np.nditer(arr2[:, ::2]):
    print(xy)

# enumerate iteration using ndenumrate() method
for index, j in np.ndenumerate(arr3):
    print(index, j)
