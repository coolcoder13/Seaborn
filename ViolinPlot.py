# Seaborn

# VIOLIN PLOT

import seaborn as sns

# iris is already saved dataset in seaborn library

iris = sns.load_dataset('iris')
iris.head()

z=iris.head(50)
sns.violinplot(y="sepal_length", x="petal_width", data=z,palette='rainbow',split=True)