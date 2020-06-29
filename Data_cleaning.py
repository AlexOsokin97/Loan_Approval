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

data_train = import_data('train_ctrUa4K.csv')
data_test = import_data('test_lAUu6dG.csv')
data = pd.concat([data_train, data_test], axis=0, ignore_index=True)
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

#### ----> ['LoanAmount_Term'] 
# I decided to create  a loan term dictionary because the loan term is affected by the loan amount that was taken and by the income of 
#the applicant/applicant + co applicant. The reason they both/each affect the loan term is because if loan amount is bigger then loan term would be longer
#while if the loan amount is smaller then loan term would be shorter. In addition, if income is larger then loan term would be shorter while if income
#is smaller then loan term would be longer. 

#To conclude, although there are not too many missing loan terms (2%) I still need to replace them with respect to the loan amount taken and the 
#borrower's income to get accurate replacement

loan_term_dic ={'Avg. LoanAmount': 
                   (df['LoanAmount'].loc[df['Loan_Amount_Term'] == 480].mean(), df['LoanAmount'].loc[df['Loan_Amount_Term'] == 360].mean(),
                   df['LoanAmount'].loc[df['Loan_Amount_Term'] == 350].mean(), df['LoanAmount'].loc[df['Loan_Amount_Term'] == 300].mean(),
                   df['LoanAmount'].loc[df['Loan_Amount_Term'] == 240].mean(), df['LoanAmount'].loc[df['Loan_Amount_Term'] == 180].mean(),
                   df['LoanAmount'].loc[df['Loan_Amount_Term'] == 120].mean(), df['LoanAmount'].loc[df['Loan_Amount_Term'] == 84].mean(),
                   df['LoanAmount'].loc[df['Loan_Amount_Term'] == 60].mean(), df['LoanAmount'].loc[df['Loan_Amount_Term'] == 36].mean(),
                   df['LoanAmount'].loc[df['Loan_Amount_Term'] == 12].mean(), df['LoanAmount'].loc[df['Loan_Amount_Term'] == 6].mean()),
                   
                'Avg. Income':
                     ((df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 480] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 480]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 360] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 360]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 350] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 350]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 300] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 300]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 240] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 240]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 180] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 180]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 120] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 120]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 84] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 84]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 60] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 60]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 36] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 36]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 12] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 12]).mean(),
                     (df['ApplicantIncome'].loc[df['Loan_Amount_Term'] == 6] + df['CoapplicantIncome'].loc[df['Loan_Amount_Term'] == 6]).mean()),
                     
                'Loan_Term_Months': ('480 months', '360 months','350 months', '300 months', '240 months', '180 months', 
                                     '120 months', '84 months', '60 months', '36 months', '12 months', '6 months') }
                    
loan_term_dic = pd.DataFrame(loan_term_dic)
                  
loan_term_nans = df.loc[pd.isnull(df['Loan_Amount_Term'])]

indxes = [19,36,44,45,73,112,165,197,223,232,335,367,421,423, 659, 662, 731, 743, 798, 828]
months = [60, 84, 36, 36, 36, 180, 240, 60, 300, 36, 24, 60, 180, 84, 60, 240, 120, 84, 240, 60]

def fill_loanTerm(data, col, indx, values):
    j = 0
    for i in indx:
        data[col].iloc[i] = values[j]
        j += 1
    return data

df1 = fill_loanTerm(df, 'Loan_Amount_Term', indxes, months)

df_nans = get_nans(df1)

#### ----> ['Credit_History'] replacing nans with mode

credit_history_mode = df1['Credit_History'].mode().iloc[0]

df1['Credit_History'].fillna(credit_history_mode, inplace=True)

df_nans = get_nans(df1)

#### ----> creating a new column that shows if a loan was taking by a single borrower or by a couple of people

df1['Num_of_Borrowers'] = df1.apply(lambda x: 2 if x['CoapplicantIncome'] != 0 else 1, axis=1)
df1 = df1[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'Num_of_Borrowers',
         'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']]
cols = get_cols(df1)
data_dtype = get_dtypes(df1, cols)

#### ----> changing cols data type

df1.iloc[:, [0, 1, 2, 3, 4, 11, 12]] = df1.iloc[:, [0, 1, 2, 3, 4, 11, 12]].astype('category')

#### ----> creating and saving new datasets

df1.to_csv('Data_EDA.csv')

datas = np.split(df1, [614])

train = datas[0]
test = datas[1]

train.to_csv('train.csv')
test.to_csv('test.csv')







