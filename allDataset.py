import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from flask import jsonify,  json
from flask import Response
from flask import Flask, make_response
from json import dumps


def giveNPDataforLaunderingAndNormalCases():

    random.seed(50)
    
    # Importing the dataset
    dataset = pd.read_csv('/media/cyris/Studies/Hackathons/CodeGrind17/Techfest April 17th/Datasets/kaggle/kaggleData.csv')
    
    dataset.drop('step', axis=1, inplace=True)
    dataset.drop('type', axis=1, inplace=True)
    dataset.drop('amount', axis=1, inplace=True)
    dataset.drop('nameOrig', axis=1, inplace=True)
    dataset.drop('oldbalanceOrg', axis=1, inplace=True)
    #dataset.drop('newbalanceOrig', axis=1, inplace=True)
    dataset.drop('nameDest', axis=1, inplace=True)
    #dataset.drop('oldbalanceDest', axis=1, inplace=True)
    #dataset.drop('newbalanceDest', axis=1, inplace=True)
    #dataset.drop('isFraud', axis=1, inplace=True)
    dataset.drop('isFlaggedFraud', axis=1, inplace=True)
    
    
    #now data has this format
    #step,type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFraud,
    # 0 , 1   , 2   ,     3      ,      4       ,      5      ,      6       ,   7   ,    
    
    sample_dataframe = dataset.sample(n=100000)
    #X = sample_dataframe.iloc[:, :-1].values
    #y = sample_dataframe.iloc[:, 7].values
    
    laundering_data_frame = sample_dataframe.loc[sample_dataframe['isFraud'] == 1]
    normal_data_frame = sample_dataframe.loc[sample_dataframe['isFraud'] == 0]
    
    #laundering_data_frame = laundering_data_frame.loc[:,1:3].values
    
    laundering_data_frame.drop(['isFraud'], axis = 1, inplace = True)
    normal_data_frame.drop(['isFraud'], axis = 1, inplace = True)
    normal_data_frame = normal_data_frame[:200]
    
    
    dataset2 = pd.read_csv('/media/cyris/Studies/Hackathons/CodeGrind17/Techfest April 17th/Datasets/kaggle/launderingCases.csv')
    sample_dataframe2 = dataset2.sample()
    
    np_launderingArray =  sample_dataframe2.values
    np_normalArray = normal_data_frame.values
    listl1 =[]
    
    for item in np_launderingArray:
        #print("item :",item)
        print("item :", item[0], ":",item[1], ":",item[2])
        listl1.append(item)
    
    #print("Laundering data dataframe :")
    #print(sample_dataframe2)
    
    #print("Laundering data numpy array :")
    #print(listl1)

    result = {"launderingCases": np_launderingArray, "normalCases": np_normalArray}
    #return Response(json.dumps(result), mimetype='application/json')
    #return make_response(dumps(np_launderingArray))

giveNPDataforLaunderingAndNormalCases()

#laundering_data_frame = laundering_data_frame.loc[:,:-1].values
#normal_data_frame = laundering_data_frame.loc[:200,:-1].values

#laundering_data_frame.drop('isFraud', axis=1)
#normal_data_frame.drop('isFraud', axis=1)

'''
print("orignial data fraud cases ",sample_dataframe.isFraud.value_counts())# -*- coding: utf-8 -*-
print("originaldata total cases",  len(sample_dataframe.index))

print("laundering data fraud cases ", laundering_data_frame.isFraud.value_counts())
print("laundering data total cases",len(laundering_data_frame.index))

print("normal data fraud cases ", normal_data_frame.isFraud.value_counts())
print("normal data total cases",len(normal_data_frame.index))
'''

#laundering_data_frame = laundering_data_frame[['newbalanceOrig','oldbalanceDest','newbalanceDest']]
#normal_data_frame = normal_data_frame[['newbalanceOrig','oldbalanceDest','newbalanceDest']]





#uncomment these lines to print files in csv format for money laundering as well as normal cases. 
#laundering_data_frame.to_csv('/media/cyris/Studies/Hackathons/CodeGrind17/Techfest April 17th/Datasets/kaggle/launderingCases.csv', sep=',', index=False)
#normal_data_frame.to_csv('/media/cyris/Studies/Hackathons/CodeGrind17/Techfest April 17th/Datasets/kaggle/normalCases.csv', sep=',', index=False)



