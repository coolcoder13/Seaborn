# Seaborn

# Distribution plots

#- distplot
#- joinplot
#- pairplot

# DIST PLOT
# dist plot is same as histogram

import seaborn as sns

# iris is already saved dataset in seaborn library

iris = sns.load_dataset('iris')
iris.head()

sns.distplot(iris['sepal_length'],color='r')

sns.distplot(iris['sepal_length'],bins=20,kde=False,color='g')
# kde = kernel density expression