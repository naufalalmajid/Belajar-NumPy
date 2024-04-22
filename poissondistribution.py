# poisson distribution is a discrete distribuiton, it estimates how many times an event can happen in a specified time
# lam rate or known number of occurences
# size is the shape of the returned array
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.poisson(lam=2, size=8)
print(x)

sns.distplot(random.normal(loc=10, scale=1, size=1000), hist=False, label="normal")
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label="binomial")
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label="poisson")

plt.show()
