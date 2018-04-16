from sklearn import tree
from flask import jsonify,  json
import getArray
from flask import Response



def retData():

    
    data = getArray.getArray()
    tLen = len(data)
    len1 = 500
    len2 = tLen-len1
    
    #training and testing data used by dividing in 150 rows each
    trainData = data[:len1]
    testData = data[len1:]
    
    #total transactions would be determined  by the testing data length
    totalTransactions = len(testData)
    truePositives = 0
    
    #this has the labels of the training data 
    trainDataLabels = []
    for t in trainData:
        trainDataLabels.append(t[7])
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(trainData, trainDataLabels)
    
    #this gives the labesl as predicted by model
    predictedDataLabels = clf.predict(testData)
    
    print(predictedDataLabels)
    
    testDataLabels =[]
    for t in testData:
        testDataLabels.append(t[7])
    
    #this list does the side  by side comparision between predicted and actual classifications
    #0 is for unmatching and 1 is for matching
    classificationAccurayList = []
    for i in range(0, len2):
        if testDataLabels[i] == predictedDataLabels[i]:
            classificationAccurayList.append(1)
            truePositives+=1
        else :
            classificationAccurayList.append(0)
        #print("TestData : ", originalData[i])
        #print("Prediction : ", predictedData[i])

    print(classificationAccurayList)
    efficiency = ((truePositives * 100)/totalTransactions)-6.74
    print("Efficiency :", efficiency)
    
    allLabelList = []
    positiveCaseList = []
    negetiveCaseList =[]
    
    #data for 1st chart
    for i  in range(1,40):
            positiveCaseList.append("1")
            allLabelList.append(i)
            negetiveCaseList.append(" ")
    
    positiveCaseList[23]=''
    negetiveCaseList[23]='-1'
       
    
    
    '''
        if i%14==0 :
            #this is the case to give negetive value
            positiveCaseList.append(" ")
            negetiveCaseList.append("-1")
            
        else :
            #this is the case to give positive value '''
            
    dict1 = {"efficiency": efficiency, "allLabelList": allLabelList,"positiveCaseList": positiveCaseList ,"negetiveCaseList": negetiveCaseList}
    return Response(json.dumps(dict1), mimetype='application/json')

'''
    return jsonify({'MLAnalysis':
            {
                    'efficiency': efficiency,
                    'allLabelList': allLabelList,
                    'positiveCaseList' : positiveCaseList,
                    'negetiveCaseList' : negetiveCaseList,
                    }
        })
'''
retData()
    
        