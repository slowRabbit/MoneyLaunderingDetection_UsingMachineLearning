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
dataset.drop('type', axis=1, inplace=True)
dataset.drop('nameOrig', axis=1, inplace=True)
dataset.drop('oldbalanceOrg', axis=1, inplace=True)
dataset.drop('newbalanceOrig', axis=1, inplace=True)
dataset.drop('nameDest', axis=1, inplace=True)
dataset.drop('oldbalanceDest', axis=1, inplace=True)
dataset.drop('newbalanceDest', axis=1, inplace=True)
dataset.drop('isFraud', axis=1, inplace=True)
dataset.drop('isFlaggedFraud', axis=1, inplace=True)

#remaining only   ->   step,,amount,,,,,,,,
#now data has this format
#step,type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFraud,
# 0 , 1   , 2   ,     3      ,      4       ,      5      ,      6       ,   7   ,    

sample_dataframe = dataset.sample(n=100)
#operations on original data, having seperated yello(laundering cases) dots
X = sample_dataframe.iloc[:, :].values
#X = sample_dataframe.iloc[:, :-1].values
#y = sample_dataframe.iloc[:, 7].values

# Encoding categorical data
labelencoder = LabelEncoder()
X[:, 1] = labelencoder.fit_transform(X[:, 1])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()




import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

X = np.array(X)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

colors = ["g.","r.","c.","y."]

for i in range(len(X)):
    #print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()


