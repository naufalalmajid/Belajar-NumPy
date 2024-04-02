# in NumPy we have data types
# we can check data types by using dtype
import numpy as np

arr = np.array([2, 8, 222, 888])
print(arr.dtype)

brand = np.array(["Toyota", "Ford", "Nissan"])
print(brand.dtype)

# creating arrays with a defined data type
# creating array with data type string by using dtype and for i, u, f, S and U we can define size as well
yearold = np.array([2002, 2024], dtype="S")
print(yearold, yearold.dtype)

# converting data type on existing arrays by using astype() method
yearoldInt = yearold.astype(int)
print(yearoldInt, yearoldInt.dtype)
