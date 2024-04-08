# data distribution is a list of all posible values an how often each value occurs
# random distribution mean set rabndom numbers that follow a certain probability desity function
from numpy import random

threeSide = random.choice([8, 28, 222], p=[0.1, 0.5, 0.4], size=(5))
print(threeSide)

fiveSide = random.choice(
    [8, 28, 222, 555, 2222], p=[0.1, 0.1, 0.3, 0.3, 0.2], size=(3, 5)
)
print(fiveSide)
