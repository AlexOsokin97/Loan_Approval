# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:26:16 2020

@author: User
"""

import pandas as pd
import numpy as np

data = pd.read_csv('loan.csv')

df = data.head(10)

nans = {'Amount':data.isna().sum() , 'Percentage':(data.isna().sum()/len(data))*100}
nans = pd.DataFrame(nans)

