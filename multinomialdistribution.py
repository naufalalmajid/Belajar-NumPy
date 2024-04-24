# multinomial distribution is a generelization of binomial distribution
# n number of possible outcomes
# pvals list of probabilities
# size the shape of returned array
from numpy import random

coin = random.multinomial(n=1, pvals=[4 / 5, 1 / 5])
print(coin)
