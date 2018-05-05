import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.svm import LinearSVC
'''
from imblearn.under_sampling import NearMiss
from imblearn import over_sampling as os
from imblearn.pipeline import make_pipeline
from imblearn.combine import SMOTETomek
from imblearn.over_sampling import ADASYN
from imblearn.under_sampling import ClusterCentroids
from imblearn.over_sampling import RandomOverSampler

from imblearn.metrics import classification_report_imbalanced
'''


random.seed(50)

# Importing the dataset
dataset = pd.read_csv('/media/cyris/Studies/Hackathons/CodeGrind17/Techfest April 17th/Datasets/kaggle/kaggleData.csv')
dataset.drop('nameOrig', axis=1, inplace=True)
dataset.drop('nameDest', axis=1, inplace=True)
dataset.drop('isFlaggedFraud', axis=1, inplace=True)

#now data has this format
#step,type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFraud,
# 0 , 1   , 2   ,     3      ,      4       ,      5      ,      6       ,   7   ,    

sample_dataframe = dataset.sample(n=100000)
X = sample_dataframe.iloc[:, :-1].values
y = sample_dataframe.iloc[:, 7].values

new_frame = sample_dataframe.loc[sample_dataframe['isFraud'] == 1]

print("orignial data fraud cases ",sample_dataframe.isFraud.value_counts())# -*- coding: utf-8 -*-
print("originaldata total cases",  len(sample_dataframe.index))
print("new data fraud cases ", new_frame.isFraud.value_counts())
print("new data total cases",len(new_frame.index))


new_frame.to_csv('/media/cyris/Studies/Hackathons/CodeGrind17/Techfest April 17th/Datasets/kaggle/moneyLaunderingCases.csv', sep=',')