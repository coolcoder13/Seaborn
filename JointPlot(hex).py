# Seaborn

# Distribution plots

#- distplot
#- joinplot
#- pairplot

# JOINT PLOT (kind='hex')

import seaborn as sns

# iris is already saved dataset in seaborn library

iris = sns.load_dataset('iris')
iris.head()

sns.jointplot(x='sepal_length',y='petal_width',data=iris,kind='hex')