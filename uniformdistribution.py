# uniform distribution used to describe where every event has equal chances of occuring
# a lower bound default 0.0
# b upper bound default 1.0
# size the shape of returned array
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

uniform = random.uniform(size=(2, 8))
print(uniform)

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()
