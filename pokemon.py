import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

pokemon =pd.read_csv('pokemon.csv')

pokemon.head()

pokemon.info()

pokemon.tail()

pokemon.columns

pokemon.shape

pokemon.describe()

pokemon.corr() #correlation 

#correlation map 
f,ax = plt.subplots(figsize=(10, 10))
sns.heatmap(pokemon.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()

#line plot
pokemon.Speed.plot(kind = 'line', color = 'g',label = 'Speed',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
pokemon.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')
plt.legend(loc='upper right')    
plt.xlabel('x axis')              
plt.ylabel('y axis')
plt.title('Line Plot')            
print(plt.show())

#scatter plot
pokemon.plot(kind='scatter', x='Attack', y='Defense',alpha = 0.5,color = 'red')
plt.xlabel('Attack')              
plt.ylabel('Defence')
plt.title('Attack Defense Scatter Plot') 
print(plt.show())

#histogram
pokemon.Speed.plot(kind = 'hist',bins = 50,figsize = (12,12))
print(plt.show())

#♣Filtering pandas data frame 
x = pokemon['Attack']>100
print(x)

#Filtering with logical_and
pokemon[np.logical_and(pokemon['Defense']>150, pokemon['Attack']>100 )]

#Hierarchical indexing
pokemon1 = pokemon.set_index(["Type 1","Type 2"]) 
pokemon1.head(10)


