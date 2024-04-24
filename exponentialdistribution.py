# exponential distribution is used for describing time till next event
# scale inverse of rate
# size the shape of the returned array
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

exp = random.exponential(scale=2, size=(2, 8))
print(exp)

sns.distplot(random.exponential(size=1000), hist=False)
plt.show()
