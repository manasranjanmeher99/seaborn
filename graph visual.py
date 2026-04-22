import warnings
warnings.filterwarnings("ignore", category=FutureWarning) 

import seaborn as sns
import pandas as pd
sns.get_dataset_names()
tips = sns.load_dataset("tips")

sns.set_theme(style="darkgrid")

tips.to_csv("tips_dataset.csv", index=False)

import os
os.getcwd()
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))


# 1. scatter plot

sns.scatterplot(data=tips, x="total_bill", y="tip",hue="time", size="size", palette="deep")
plt.title("Scatterplot of Total Bill vs Tip")
plt.show()

# 2.line plot

sns.lineplot(data=tips, x= 'size', y='total_bill', hue='sex',markers='o')
plt.title("Lineplot of Total Bill vs Size")
plt.show()

sns.lineplot(data=tips, x= 'size', y='total_bill', hue='sex',ci=None, markers='0')
plt.title("Lineplot of Total Bill vs Size")
plt.show()

#3. bar plot

sns.barplot(data=tips, x='day', y='total_bill', hue = 'sex',palette='muted')
plt.title("Barplot of Total Bill by Day")
plt.show()

# 4. Boxplot 

sns.boxplot(data=tips, x='day', y='tip', hue='smoker', palette='Set2')
plt.title("Boxplot of Tips by Day and Smoker Status")
plt.show()

# 5. violin plot 

sns.violinplot(data=tips, x='day', y='total_bill', hue='time', split=True, palette='pastel')
plt.title("Violin Plot of Total Bill by Day and Time")  
plt.show()

#6. count plot: Order by day, split by smoker

sns.countplot(data=tips, x='day', hue='smoker', palette='dark')
plt.title("Count Plot of Days by Smoker Status")
plt.show()


#7. regression plot: Total Bill vs Tips With regression line

sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title("Regression Plot of Total Bill vs Tip")   
plt.show()

# 8. Histogram of total bill with KDE

sns.histplot(data=tips, x='total_bill', bins=20, kde=True, color='blue')
plt.title("Histogram of Total Bill with KDE")
plt.show()

#9. pairplot: RelationShip between numberical variable

sns.pairplot(tips, hue='sex', vars=["total_bill", "tip", "size"], palette='husl')
plt.suptitle("pair plot: numerberic variables by gender", y=1.02)
plt.show()

# 10 catplot: (Point plot) Tips by day

sns.catplot(data=tips, x='day', y='tip', hue='sex', kind='point', palette='bright')
plt.title("catplot(point):Tips by day and gender")
plt.show()

# 11. jointplot

sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter', hue='smoker', color='purple', palette='coolwarm')
plt.suptitle("Jointplot: Total Bill vs Tip", y=1.02)
plt.show()

# 12. Facetgrid: Total bill by Time and smoke

g = sns.FacetGrid(tips, col='time', row='smoker', margin_titles=True).map(sns.histplot, 'total_bill', bins=20, kde=True).add_legend()
plt.suptitle("facetgrid: Total Bill by Time and Somker", y=1.02)
g


#13. strip plot

sns.stripplot(data=tips, x='day', y='tip', hue='sex', jitter=True, palette='Set1')
plt.title("strip plot: Tips by data and gender")
plt.show()

# 14. KDE PLOT: Total Bill density by gender

sns.kdeplot(data=tips, x='total_bill',hue='sex', fill=True, palette='tab10')
plt.title("kde plot:Total bill density by gender")
plt.show()
