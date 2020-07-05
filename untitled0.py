# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 00:42:57 2020

@author: Alexander
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_data(path):
    data = pd.read_csv(path)
    return data

data = get_data('./train_test_result/train.csv')
data.drop(['Unnamed: 0'], axis=1, inplace=True)

df_dums = pd.get_dummies(data)

X = df_dums.drop(['Gender_Male', 'Married_Yes', 'Dependents_3+', 'Education_Not Graduate',
                  'Self_Employed_Yes', 'Property_Area_Urban', 'Loan_Status_N','Loan_Status_Y'],
                 axis=1).values

y = df_dums['Loan_Status_Y'].values

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, plot_confusion_matrix
import pickle

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=35)

def cross_validation(model, train_features, train_label, scoring, cv):
    avg_score = np.mean(cross_val_score(model, train_features, y=train_label, scoring=scoring, cv=cv))
    return avg_score

def grid_search(model, train_features, train_label,params, scoring, cv):
    gs = GridSearchCV(estimator=model, param_grid=params, scoring=scoring, cv=cv)
    gs.fit(train_features, train_label)
    best_find = gs.best_estimator_
    best_score = gs.best_score_
    return best_find, best_score

def save_model(model, name):
    filename = name+".sav"
    pickle.dump(model, open(filename, 'wb'))

def model_performance(model,test_features, test_label):
        y_pred = model.predict(test_features)
        f1 = f1_score(y_true=test_label, y_pred=y_pred, average='binary')
        accuracy = accuracy_score(y_true=test_label, y_pred=y_pred)
        conf = plot_confusion_matrix(model, test_features, test_label)
        return f1, accuracy

####################################################################################################
rfc = RandomForestClassifier()

rfc_val_score = cross_validation(rfc, X_train, y_train, 'accuracy', 5)

rfc_params = [{'n_estimators': (50,100,150,200), 'criterion':('gini','entropy'), 
               'max_depth': (2,4,6,8), 'min_samples_split': (2,4,6,8), 
               'min_samples_leaf':(1,3,5,7), 'max_features':('auto', 'sqrt','log2')}]

rfc_best_model, rfc_best_score = grid_search(rfc, X_train, y_train, rfc_params, 'accuracy', 3)

rfc_f1_score, rfc_pred_accuracy = model_performance(rfc_best_model, X_test, y_test)

####################################################################################################

xg = XGBClassifier()

xg_val_score = cross_validation(xg, X_train, y_train, 'accuracy', 5)

xg_params = [{'max_depth':(2,4,6), 'learning_rate':(0.001,0.01,0.1), 'n_estimators': range(50,200,50)}]

xgb_best_model, xgb_best_score = grid_search(xg, X_train, y_train, xg_params, 'accuracy', 3)

xg_f1_score, xg_pred_accuracy = model_performance(xgb_best_model, X_test, y_test)

####################################################################################################

gb = GradientBoostingClassifier()

gb_val_score = cross_validation(gb, X_train, y_train, 'accuracy', 5)

gb_params = [{''}]





















