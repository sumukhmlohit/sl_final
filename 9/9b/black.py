import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('blackfri.csv')

print(df.head())
print(df.describe())

df['City_Category']=df['City_Category'].fillna('A')

df['City_Category']=df['City_Category'].map({'A':'Metro Cities','B':'Small Towns','C':'Villages'})
print(df.head())
print(df['City_Category'])

ax=sns.countplot(x='Gender',hue='City_Category',data=df)
ax.set(title='Gender vs city cat.',xlabel='Gender',ylabel='City Category')
plt.show()
