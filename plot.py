import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_pickle("family_data1.pkl")
data2 = pd.read_pickle("family_data2.pkl")
data3 = pd.read_pickle("family_data3.pkl")

fig, ax = plt.subplots(figsize = (5, 3))

#sns.barplot(ax=ax, x='frequency',y='word',data=data1.head(5))
sns.barplot(ax=ax, x='frequency',y='pairs',data=data2.head(5))
#sns.barplot(ax=ax, x='frequency',y='trigrams',data=data3.head(5))

ax.set_xlabel("Frequency", size=14)
ax.set_ylabel("Pairs of Words", size=14)
ax.set_title('Frequency of Pairs of Words in Unanswered Questions in "Other" Category',
             size=18)
ax.set_xticklabels(ax.get_xticks().astype(int), size = 12)
ax.set_yticklabels(ax.get_yticklabels(), size = 12)

plt.show()

print(data2[:5])
print(data2["frequency"].sum())
print(data2["pairs"].count())
