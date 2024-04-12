# binomial distribution is a discrete distribution which it is defined as separate set of events e.g. a coin toss's result
# n number of trials
# p probability of occurence of each trial
# size shape of the returned array
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.binomial(n=10, p=0.5, size=10)
print(x)

# visualization of binomial distribution and difference with normal distribution
sns.distplot(
    random.normal(loc=50, scale=5, size=1000), hist=False, label="Normal Distribution"
)
sns.distplot(
    random.binomial(n=100, p=0.5, size=1000), hist=False, label="Binomial Distribution"
)
plt.show()
