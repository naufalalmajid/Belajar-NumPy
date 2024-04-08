# a permutations refers to an arrangement of elements
# shuffling arrays, by using shuffle() method it is makes changes to the original array
from numpy import random
import numpy as np

arr = np.array([28, 99, 222, 555, 222])
random.shuffle(arr)

print(arr)

# generating permutations of arrays, by using permutation() method it is meaning returns a re-arranged array and still have original array
base = np.array([28, 88, 222, 555, 2222])
print(random.permutation(base))
