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
from json import dumps# -*- coding: utf-8 -*-


def dataSetForRepresentation():

    dataset2 = pd.read_csv('/media/cyris/Studies/Hackathons/CodeGrind17/Techfest April 17th/Datasets/kaggle/launderingCases.csv')
    sample_dataframe2 = dataset2.sample(n=120)
        
    np_launderingArray =  sample_dataframe2.values
    listl1 = []
    
    for item in np_launderingArray:
        #print("item :",item)
        #print("item :", item[0], ":",item[1], ":",item[2])
        listl1.append(item)
        
    #print("Laundering data dataframe :")
    #print(sample_dataframe2)
    
    #print("Laundering data listl1 :")
    #print(listl1)
    
    result = {"launderingCases": listl1}
    #return Response(json.dumps(result), mimetype='application/json')
    return jsonify({'MLAnalysis':
            {
                    'launderingCases': listl1.tolist(),
                    }
        })

