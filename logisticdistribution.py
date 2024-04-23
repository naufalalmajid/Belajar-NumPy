# logistic distribution is used to describe growth, which it's used extensively in machine learning in logistic regression, neural networks etc.
# loc mean where the peak default 0
# scale standard deviation, the flatness of distribution default 1
# size the shape of returning array
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

logistic = random.logistic(loc=1, scale=2, size=(2, 8))
print(logistic)

sns.distplot(random.normal(scale=2, size=1000), hist=False, label="normal")
sns.distplot(random.logistic(size=1000), hist=False, label="logistic")

plt.show()
