# getting some elements out of an existing array and creating a new array out(filtering)
# in numpy we can filter an array using a boolean index list
import numpy as np

yearOld = np.array([2002, 2024, 21])
x = [True, False, True]
newArr = yearOld[x]
print(newArr)

# creating the filter array
arr = np.array([2, 8, 28, 99, 222, 555, 2222])
filterArr = []

for value in arr:
    if value >= 28:
        filterArr.append(True)
    else:
        filterArr.append(False)


newValue = arr[filterArr]
print(filterArr)
print(newValue)

# creating filter directly from array
diretctArr = arr >= 28
newArrdirect = arr[diretctArr]

print(diretctArr)
print(newArrdirect)
