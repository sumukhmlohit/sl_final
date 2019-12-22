import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('stud.csv')
print(df.head(5))
print(df.describe())

print('info')
print(df.info())
df.drop(columns=['lunch'],inplace=True)
df['parental level of education']=df['parental level of education'].fillna('No degree')
print(df.head())
print(df.info())

ax=sns.countplot(x='gender',hue='test_preparation_course',data=df)
ax.set(title='Gender vs test prep status',xlabel="Gender",ylabel="Course status")
plt.show()
