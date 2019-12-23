import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('iris.csv')
print(df.head(5))
print(df.describe())
print('Mean petal width:')
print(df.groupby(['Class']).mean())

ax=sns.countplot(x='Class',hue=' Sepal_Width',data=df)
ax.set(title='Class vs sep width',xlabel='Class',ylabel='sepwidth')
plt.show()
