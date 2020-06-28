# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:41:12 2020

@author: Alexander
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def import_data(path):
    data = pd.read_csv(path)
    return data

def get_nans(data):
    na_sum = data.isna().sum()
    nans = {'Amount': na_sum, 'Percentage': (na_sum/len(data))*100}
    nans = pd.DataFrame(nans)
    return nans
    
def get_cols(data):
    cols = data.columns
    return cols

def get_values(data, cols):
    dic = {}
    for col in cols:
        dic[col] = data[col].unique()
    return dic

def get_dtypes(data, cols):
    d_type = {}
    for col in cols:
        d_type[col] = str(data[col].dtype)
    return d_type

def get_copy(data):
    copy = data.copy()
    return copy

data = import_data('train_ctrUa4K.csv')
nans = get_nans(data)
cols = get_cols(data)
vals = get_values(data, cols)
data_dtype = get_dtypes(data, cols)
df = get_copy(data)

#### ---> [Gender] replacing nans with the mode

gender_mode = df['Gender'].mode().iloc[0]

df['Gender'].fillna(gender_mode, inplace=True)

df_nans = get_nans(df)

#### ----> [Married] replacing nans with the mode

married_mode = df['Married'].mode().iloc[0]

df['Married'].fillna(married_mode, inplace=True)

df_nans = get_nans(df)

#### ----> ['Dependents'] replacing nans with the mode

dependents_mode = df['Dependents'].mode().iloc[0]

df['Dependents'].fillna(dependents_mode, inplace=True)

df_nans = get_nans(df)

#### ----> ['selfEmployed'] replacing nans with the mode

self_Employed_mode = df['Self_Employed'].mode().iloc[0]

df['Self_Employed'].fillna(self_Employed_mode, inplace=True)

df_nans = get_nans(df)

#### ----> ['LoanAmount'] replacing nans with mean (i chose education as mean criterion because those who have education most likely
####                                                have a job and could afford a higher loan amount)

graduated_mean = df['LoanAmount'].loc[df['Education'] == 'Graduate'].mean()
ungraduated_mean = df['LoanAmount'].loc[df['Education'] == 'Not Graduate'].mean()


df['LoanAmount'] = df.apply(lambda x: graduated_mean if x['Education']=='Graduate' and 
                            pd.isna(x['LoanAmount']) else x['LoanAmount'], axis=1)
df['LoanAmount'] = df.apply(lambda x: ungraduated_mean if x['Education']=='Not Graduate' and 
                            pd.isna(x['LoanAmount']) else x['LoanAmount'], axis=1)

df_nans = get_nans(df)

#### ----> ['LoanAmount_Term'] replacing nans with median

loan_term_dic ={'480months LoanAmount & Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 480].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 480] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 480]).mean()),
                   
               '360months LoanAmount & Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 360].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 360] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 360]).mean()),
                                     
               '300months LoanAmount & Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 300].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 300] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 300]).mean()),
                   
               '240months LoanAmount& Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 240].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 240] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 240]).mean()),
                   
               '180months LoanAmount& Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 180].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 180] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 180]).mean()),
                                     
               '120months LoanAmount & Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 120].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 120] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 120]).mean()),
                                     
               '084months LoanAmount & Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 84].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 84] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 84]).mean()),
                                     
               '060months LoanAmount & Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 60].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 60] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 60]).mean()),
                                     
               '036months LoanAmount & Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 36].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 36] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 36]).mean()),
                                     
               '012months LoanAmount & Avg.Income': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 12].mean(),
                    (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 12] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 12]).mean())}

















