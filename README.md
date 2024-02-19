# About

Post-Graduate Challenge in Data Analysis using Seaborn

## Pairwise Relationships

The script `pairwise_relationships.py` generates a paired relationship plot that crosses information on the number of bedrooms, number of bathrooms, parking spaces, and total rent. The data is colored by the city of the property.

![Pairwise Relationships](result/pairwise_relationship.png)

From the analysis of these relationships, it is observed, for example, in the fourth graph of the first row, that the city with the highest rent for a one-bedroom property is São Paulo.

## Faceted Graph of Number of Bedrooms by City

The script `faceted_graphic.py` constructs a faceted graph by city mapping the number of bedrooms each city has. For this, the `sns.countplot` function was used as visualization for the subplots.

![Number of Bedrooms by City](result/faceted_graphic.png)

One result observed in the graph is the most frequent number of bedrooms in the apartments available in each of the cities. There are 3 bedrooms in São Paulo, Campinas, and Belo Horizonte, and 2 bedrooms in Porto Alegre and Rio de Janeiro.

## Faceted Graph of Rent Price, by City, by Acceptance of Pets

The script `animal_scatter.py` constructs a faceted graph by cities (columns) and by the animal variable (rows) with the distribution of the total rent value.

![Relationship between Rent Price and Acceptance of Pets](result/animal_scatter.png)

The graph allows us to analyze if there is any relationship between the rent price and whether the condominium accepts pets, but the lack of density hinders the analysis.

Therefore, the script `animal_swarm.py` was created to observe the density of the values.

![Relationship between Rent Price and Acceptance of Pets Exposing Data Density](result/animal_swarm.png)

The graph with the data densities allows for a better conclusion of the relationship between the rent price and whether the condominium accepts pets. It is concluded that the number of apartments with higher rent values that accept pets is greater than the number that does not.
