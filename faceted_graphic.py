import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('rent.csv')

facet = sns.FacetGrid(df, col="city")
facet.map(sns.countplot, "rooms")

plt.savefig('result/faceted_graphic.png')
