# Seaborn

# COUNT PLOT

import seaborn as sns

# iris is already saved dataset in seaborn library

iris = sns.load_dataset('iris')
iris.head()

sns.countplot('sepal_length',data=iris)

sns.countplot(y='sepal_length',data=iris)