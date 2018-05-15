from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


'''
iris = load_iris()
#X_tsne = TSNE(learning_rate=100).fit_transform(iris.data)
X_tsne = TSNE(learning_rate=160).fit_transform(samp2)
X_pca = PCA().fit_transform(iris.data)

plt.figure(figsize=(10, 5))
plt.subplot(121)
#plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=iris.target)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=spec)
'''

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
dataset = pd.read_csv('D:\Hackathons\CodeGrind17\Techfest April 17th\Datasets\kaggle\kaggleData.csv')
dataset.drop('nameOrig', axis=1, inplace=True)
dataset.drop('nameDest', axis=1, inplace=True)
dataset.drop('isFlaggedFraud', axis=1, inplace=True)

#now data has this format
#step,type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFraud,
# 0 , 1   , 2   ,     3      ,      4       ,      5      ,      6       ,   7   ,    

sample_dataframe = dataset.sample(n=100000)
#operations on original data, having seperated yello(laundering cases) dots
X = sample_dataframe.iloc[:, :-1].values
y = sample_dataframe.iloc[:, 7].values

new_frame = sample_dataframe.loc[sample_dataframe['isFraud'] == 1]
new_frame.append(sample_dataframe)
#sample_dataframe.append(new_frame)
#now the new data has starting 112 cases of money laundering
#X = new_frame.iloc[:, :-1].values
#y = new_frame.iloc[:, 7].values

# Encoding categorical data
labelencoder = LabelEncoder()
X[:, 1] = labelencoder.fit_transform(X[:, 1])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]
X = X[0:200]
y = y[0:200]
#X = X[-300:]
#y = y[-300:]

X_tsne = TSNE(learning_rate=160).fit_transform(X)
#X_pca = PCA().fit_transform(iris.data)
X_pca = PCA().fit_transform(X)

plt.figure(figsize=(35, 15))
#plt.subplot(150)
#plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=iris.target)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)


#print ("Iris data set :")
#print (iris.data)
#plt.subplot(122)
#plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target)
