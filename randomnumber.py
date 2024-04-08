# in numpy we can generate random number
# generate random number
from numpy import random

randomValue = random.randint(222)
print(randomValue)

# generate random float
randomFloat = random.rand()
print(randomFloat)

# generate random array
randomInt = random.randint(222, size=(5))
print(randomInt)

randomInt2 = random.randint(222, size=(3, 5))
print(randomInt2)

# generate random number from array by using choice() method
randomPick = random.choice([2, 8, 28, 99, 222])
print(randomPick)
