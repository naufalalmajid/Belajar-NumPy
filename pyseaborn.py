# seaborn is a librariy that uses Matplotlib underneath to plot graphs, it will be used to visualize random distributions
# distribution plot, it take as input an array and plots a curve corresponding distribution of points in the arrays
import matplotlib.pyplot as plt
import seaborn as sns

# plotting a displot
sns.distplot([2, 4, 6, 8])

plt.show()

# in case we want displot without histogram we can use
# sns.displot([2,4,6,8],hist=False)
