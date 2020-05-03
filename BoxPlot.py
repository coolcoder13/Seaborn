# Seaborn

# BOX PLOT

import seaborn as sns

# iris is already saved dataset in seaborn library

iris = sns.load_dataset('iris')
iris.head()

z=iris.head(50)
sns.boxplot('sepal_length','petal_length',data=z,palette='rainbow')