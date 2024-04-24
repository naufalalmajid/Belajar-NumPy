# Chi Square distribution is used as a basis to verify the hypotesis
# df degree of freedom
# size the shape of the returned array
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

chi = random.chisquare(df=2, size=(2, 8))
print(chi)

sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()
