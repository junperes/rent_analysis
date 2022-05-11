import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('rent.csv')

facet = sns.FacetGrid(df, col="city")
facet.map(sns.swarmplot, "animal", "total (R$)", order=["acept", "not acept"]).add_legend()  

plt.savefig('result/animal_swarm.png')
