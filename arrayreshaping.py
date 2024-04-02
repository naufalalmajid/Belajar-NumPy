# reshaping it is mean changing the shape on an array
# reshape from 1-D to 2-D, we can reshape by using reshape attribute
import numpy as np

arr = np.array([2, 8, 28, 99, 88, 222, 888, 555, 2222, 5555, 8888, 999])
newArr = arr.reshape(4, 3)
print(newArr)

# reshape from 1-D to 3-D
newArr1 = arr.reshape(2, 2, 3)
print(newArr1)

# unknown dimension, by using -1 numpy will calculte
newArr2 = arr.reshape(3, 2, -1)
print(newArr2)

# flattening the arrays, we can using reshape(-1) for converting to 1-D arrays
newArr3 = newArr2.reshape(-1)
print(newArr3)
