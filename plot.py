import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_pickle("family_data1.pkl")
data2 = pd.read_pickle("family_data2.pkl")
data3 = pd.read_pickle("family_data3.pkl")

#sns.barplot(x='frequency',y='word',data=data1.head(30))
sns.barplot(x='frequency',y='pairs',data=data2.head(30))
#sns.barplot(x='frequency',y='trigrams',data=data3.head(30))
plt.show()