# Seaborn

# Distribution plots

#- distplot
#- joinplot
#- pairplot

# PAIR PLOT
# can be compared to multivariate analysis

import seaborn as sns

# iris is already saved dataset in seaborn library

iris = sns.load_dataset('iris')
iris.head()

sns.pairplot(iris)