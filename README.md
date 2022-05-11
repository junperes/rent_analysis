# Sobre

Desafio da Pós Graduação em Análise de Dados usando Seaborn

## Relações Pareadas

O script pairwise_relationships.py gera um gráfico de relações pareadas que cruza as informações de número de quartos, número de banheiros, vagas de garagens e o total do aluguel. Os dados são pintados pela cidade do imóvel. 

![Relações pareadas](result/pairwise_relationship.png)

A partir da análise dessas relações observa-se, por exemplo, no quarto gráfico da primeira linha, que a cidade que possui o aluguel mais caro para um imóvel de um quarto é a cidade de São Paulo.

## Gráfico Facetado do número de quartos por cidade

O script faceted_graphic constrói um gráfico facetado por cidade mapeando o número de quartos que cada cidade tem. Para isso foi utilizado como visualização dos sugráficos a classe sns.countplot. 

![Número de quartos por cidade](faceted_graphic.png)

Um resultado observado no gráfico é a quantidade de quartos mais frequente nos apartamentos disponíveis em cada uma das cidades. Sendo 3 quartos em São Paulo, Campinas e Belo Horizonte e 2 quartos em Porto Alegre e Rio de Janeiro.
