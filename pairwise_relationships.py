import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('rent.csv')

sns_plot = sns.pairplot(df,
    x_vars=["rooms", "bathroom", "parking spaces", "total (R$)"],
    y_vars=["rooms", "bathroom", "parking spaces", "total (R$)"],
    hue="city"
)
plt.savefig('result/pairwise_relationship.png')
