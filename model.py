# -*- coding: utf-8 -*-
"""
Created on Fri May 26 01:09:42 2023

@author: Sanket
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle


dataset = pd.read_csv('Composites.csv')
dataset=dataset.dropna()
dataset=dataset.drop(['No.','PoissonÕs_ratio_of_fiber','Type_of_fiber','YoungÕs_modulus_of_matrix','PoissonÕs_ratio_of_matrix','YoungÕs_modulus_of_fiber'],axis=1)
X=dataset.drop(['Fmax','IFSS'],axis=1)

y=dataset['IFSS']


#Converting words to integer values
#def convert_to_int(word):
  ##  word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
    #            'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    #return word_dict[word]

#X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

#y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.
#
from sklearn.tree import DecisionTreeRegressor

regressor=DecisionTreeRegressor(max_depth= None,
 max_features=15,
 max_leaf_nodes=40,
 min_samples_leaf=1,
 min_weight_fraction_leaf=0,
 splitter='random')

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6]]))