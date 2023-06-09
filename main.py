# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/117FdoyEfN0RvACBNtzmwQlbBzk_CIe6p
"""

from google.colab import files
dataset = files.upload()

#Importing Packages
import pandas as pd       #Useful for importing, manipulating, selection, cleaning data 
data_pd = pd.read_csv(r"/content/preprocessed data.csv")  #Reading dataset.
data_pd.head()

data_pd.dtypes            #Datatype of each attribute

data_pd.columns            #Colummns

data_pd.groupby('comment').size()

#Plot of dataset 
#Import package
import matplotlib.pyplot as plt         #Useful for graphs, plots

plt.matshow(data_pd.corr())
plt.show()

f = plt.figure(figsize=(19, 15))
plt.matshow(data_pd.corr(), fignum=f.number)
plt.xticks(range(data_pd.shape[1]), data_pd.columns, fontsize=14, rotation=45)
plt.yticks(range(data_pd.shape[1]), data_pd.columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('C',fontsize=16);

df = pd.DataFrame(data_pd)
df[['username', 'comment']]

d = {}
imp_comments = []
score = 4
search_keywords =['Interested', 'interested', 'INTERESTED', 'DM', 'dm', 'Dm', 'PRICE', 'Price', 'price', 'Promote','promote', 'PROMOTE']

for (colname,colval) in data_pd.iteritems():
  if(colname=="comment"):
    #print(colval.values)
    c = colval.values
    for sentence in c:
      for word in search_keywords:
        if(isinstance(sentence, str)):
          if word in sentence:
            #print(sentence)
            imp_comments = sentence
            d[word]=df.loc[df['comment'] == imp_comments, 'username']
            
               
        else:
          continue

def score(keywords):
  if keywords=='DM':
    print(d['DM'])
    score = 1
  elif keywords=='dm':
    print(d['dm'])
    score = 1
  elif keywords=='Dm':
    print(d['Dm'])
    score = 1
  elif keywords=='Interested':
    print(d['Interested'])
    score = 2
  elif keywords=='interested':
    print(d['interested'])
    score = 2
  elif keywords=='INTERESTED':
    print(d['INTERESTED'])
    score = 2
  elif keywords=='price':
    print(d['price'])
    score = 3
  elif keywords=='Price':
    print(d['Price'])
    score = 3
  elif keywords=='PRICE':
    print(d['PRICE'])
    score = 3
  elif keywords=='promote':
    print(d['promote'])
    score = 4
  elif keywords=='Promote':
    print(d['Promote'])
    score = 4
  elif keywords=='PROMOTE':
    print(d['PROMOTE'])
    score = 4
  print("score: ", score)

d1 = score('DM')

d2 = score('dm')

d3 = score("Dm")

d4 = score('Interested')

d5 = score('price')

d6 = score('Price')

d7 = score('promote')

d8 = score('PROMOTE')

d9 = score("Promote")