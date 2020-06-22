# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:26:16 2020

@author: User
"""

import pandas as pd
import numpy as np

data = pd.read_csv('loan.csv', low_memory=False)

df = data.head(10)

nans = {'Amount':data.isna().sum() , 'Percentage':(data.isna().sum()/len(data))*100} 

df = data.copy()

columns = df.columns

u = {}
for col in columns:
    u[col] = df[col].value_counts(dropna=False)
    
u = pd.DataFrame(u)

head = df.head()

s = df['term'].unique()


s.sizes







