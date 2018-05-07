import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from imblearn.under_sampling import NearMiss
from imblearn import over_sampling as os
from imblearn.pipeline import make_pipeline
from imblearn.combine import SMOTETomek
from imblearn.over_sampling import ADASYN
from imblearn.under_sampling import ClusterCentroids
from imblearn.over_sampling import RandomOverSampler

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
from sklearn.metrics import accuracy_score


#pipeline would be made a global variable
#pipeline4 = make_pipeline(ADASYN(),LinearSVC(random_state=1))

clf = svm.SVC(kernel='linear', C = 1.0)

def classifyOriginalDataSet():

    random.seed(50)
    pipeline4 = make_pipeline(ADASYN(),LinearSVC(random_state=1))
    
    X_trainGlobal = []
    y_trainGlobal = []
    
    # Importing the dataset
    dataset = pd.read_csv('/media/cyris/Studies/Hackathons/CodeGrind17/Techfest April 17th/Datasets/kaggle/kaggleData.csv')
    dataset.drop('nameOrig', axis=1, inplace=True)
    dataset.drop('nameDest', axis=1, inplace=True)
    dataset.drop('isFlaggedFraud', axis=1, inplace=True)
    
    #now data has this format
    #step,type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFraud,
    # 0 , 1   , 2   ,     3      ,      4       ,      5      ,      6       ,   7   ,    
    
    sample_dataframe = dataset.sample(n=40000)
    X = sample_dataframe.iloc[:, :-1].values
    y = sample_dataframe.iloc[:, 7].values
    
    print(sample_dataframe.isFraud.value_counts())
    
    
    # Encoding categorical data
    labelencoder = LabelEncoder()
    X[:, 1] = labelencoder.fit_transform(X[:, 1])
    onehotencoder = OneHotEncoder(categorical_features = [1])
    X = onehotencoder.fit_transform(X).toarray()
    
    # Avoiding the Dummy Variable Trap
    X = X[:, 1:]
    
    X1 = X[:15000, :]
    y1 = y[:15000]
    X2 = X[15002:, :]
    y2 = y[15002:]
    
    # Splitting the dataset into the Training set and Test set
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.5, random_state=1)
    
    counts = np.unique(y_train, return_counts=True)
    
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_val = sc.transform(X_val)
    X_test = sc.transform(X_test)
    print(counts)
    
    
    # Apply the sampling
    ada = ADASYN()
    X_resampled, y_resampled = ada.fit_sample(X_train, y_train)
    count = np.unique(y_resampled, return_counts=True)
    
    X_train2 = X_train
    y_train2 = X_train
    
    # Create a pipeline
    pipeline4 = make_pipeline(ADASYN(),LinearSVC(random_state=1))
    pipeline4.fit(X_train, y_train)
    print(count)
    
    predicted=pipeline4.predict(X_test)
    print (X_test.shape)
    '''
   
    
    global clf
    clf = svm.SVC(kernel='linear', C = 1.0)
    
    #y_test, pipeline4.predict(X_test))
    
    clf.fit(X1,y1)
    predicted = clf.predict(X2)
    print("value predicted")
    print("Accuracy :",accuracy_score(y2, predicted))




def classifyLive(filePath):

    dataset = pd.read_csv(filePath)
    dataset.drop('nameOrig', axis=1, inplace=True)
    dataset.drop('nameDest', axis=1, inplace=True)
    dataset.drop('isFlaggedFraud', axis=1, inplace=True)
    
    #now data has this format
    #step,type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFraud,
    # 0 , 1   , 2   ,     3      ,      4       ,      5      ,      6       ,   7   ,    
    
    sample_dataframe = dataset.sample(n=70)
    X = sample_dataframe.iloc[:, :-1].values
    y = sample_dataframe.iloc[:, 7].values
    
    print(sample_dataframe.isFraud.value_counts())
    
    
    # Encoding categorical data
    labelencoder = LabelEncoder()
    X[:, 1] = labelencoder.fit_transform(X[:, 1])
    onehotencoder = OneHotEncoder(categorical_features = [1])
    X = onehotencoder.fit_transform(X).toarray()
    
    # Avoiding the Dummy Variable Trap
    #X = X[:, 1:]
    
    #X1 = X[:2500, :]
    #y1 = y[:2500]
    #X2 = X[2502:, :]
    #y2 = y[2502:]
    
    predicted = clf.predict(X)
    print("value predicted")
    print("Accuracy2 :",accuracy_score(y, predicted))
    print("value predicted 2:")
    print(predicted)

classifyOriginalDataSet()
classifyLive('/media/cyris/Studies/Hackathons/CodeGrind17/Techfest April 17th/Datasets/kaggle/try1.csv')