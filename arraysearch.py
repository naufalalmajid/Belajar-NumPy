# we can search certain value by using where() method
# it is will be printed result as index value
import numpy as np

arr = np.array([2, 8, 28, 88, 222, 555, 888, 2222])

value28 = np.where(arr > 28)
print(value28)

# search sorted, searchsorted() method is perform a binary search in array
# and returns the index where the specified value would be inserted to maintain the search order
value2222 = np.searchsorted(arr, 2222)
print(value2222)

# search from the right side, using side="right"
value555 = np.searchsorted(arr, 555, side="right")
print(value555)

# multiple values
value2299 = np.searchsorted(arr, [22, 99])
print(value2299)
