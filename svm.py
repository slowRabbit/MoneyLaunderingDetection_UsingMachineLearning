from sklearn import tree
from flask import jsonify,  json
import getArray


def retData():

    
    data = getArray.getArray()
    
    trainData = data[:150]
    testData = data[150:]
    
    trainClassification = []
    for t in trainData:
        trainClassification.append(t[7])
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(trainData, trainClassification)
    predictedData = clf.predict(testData)
    
    print(predictedData)
    
    originalData =[]
    for t in testData:
        originalData.append(t[7])
    
    checkClassificationList = []
    for i in range(0, 150):
        if originalData[i] == predictedData[i]:
            checkClassificationList.append(1)
        else :
            checkClassificationList.append(0)
        #print("TestData : ", originalData[i])
        #print("Prediction : ", predictedData[i])

    print(checkClassificationList)
    return json.dumps(checkClassificationList)

retData()
    
        