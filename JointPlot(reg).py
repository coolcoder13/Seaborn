# Seaborn

# Distribution plots

#- distplot
#- joinplot
#- pairplot

# JOINT PLOT (kind='reg')

import seaborn as sns

# iris is already saved dataset in seaborn library

iris = sns.load_dataset('iris')
iris.head()

sns.jointplot(x='sepal_length',y='sepal_width',data=iris,kind='reg',color='g')


