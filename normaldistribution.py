# we can use random.normal() method for get a normal data distribution
# loc (mean) where the peak of the bell existx
# scale (standard deviation) how flat the graph distribution should be
# size the shape of the returned array
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

normal = random.normal(size=(2, 8))
print(normal)

normal1 = random.normal(loc=2, scale=8, size=(2, 8))
print(normal1)

# visualisation of normal distribution
sns.distplot(random.normal(size=2222), hist=False)
plt.show()
