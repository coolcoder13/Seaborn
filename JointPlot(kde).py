# Seaborn

# Distribution plots

#- distplot
#- joinplot
#- pairplot

# JOINT PLOT (kind='kde')

import seaborn as sns

# iris is already saved dataset in seaborn library

iris = sns.load_dataset('iris')
iris.head()

sns.jointplot(x='petal_length',y='petal_width',data=iris,kind='kde',color='orange')
# kde = kernel density estimation