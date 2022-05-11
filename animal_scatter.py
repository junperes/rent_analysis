import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('rent.csv')

facet = sns.FacetGrid(df, col="city")
facet.map(plt.scatter, "animal", "total (R$)").add_legend() 

plt.savefig('result/animal_scatter.png')
