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

s = df['loan_amnt'].unique()


len(s)


def get_column_values(data, columns, threshold):
    col_vals = {}
    for col in columns:
        num_uniq = data[col].unique()
        if len(num_uniq) <= threshold:
            col_vals[col] = data[col].unique()
        else:
            continue
        
    return col_vals


dic = get_column_values(df, df.columns, 1000000)
disc = pd.DataFrame(dic)

t = np.dtype(df['term'])

if t == 'O':
    print('ok')







