# sorting arrays meaning putting elements in an ordered sequence
# we can using sort() function
import numpy as np

arr = np.array([28, 999, 2222, 5555, 8888, 9999, 555, 888])
print(np.sort(arr))

brand = np.array(["Isuzu", "Toyota", "Ford", "Mitsubishi", "Lamborghini", "Nissan"])
print(np.sort(brand))

# sorting 2-D arrays
arr2 = np.array([[99, 28], [555, 2222]])
print(np.sort(arr2))
