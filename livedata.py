from sklearn import tree
from flask import jsonify,  json
import getArray
from flask import Response


launderingList = []
normalList = []


tempArrN  = [0.0,288800.0,2415.16]
normalList.append(tempArrN)
tempArrN  = [0.0,21182.0,0.0]
normalList.append(tempArrN)
tempArrN  = [29885.86,0.0,0.0]
normalList.append(tempArrN)

tempArrL  = [19384.72,676715.35,156840.93]
launderingList.append(tempArrL)
tempArrL  = [0.0,302583.81,764093.67]
launderingList.append(tempArrL)

def returnCasesList():

    
    print("launderingList :", launderingList)
    return jsonify({'Cases_List':
            {
                    'launderingList': launderingList,
                    'normalList':normalList,
                    }
        })
    
def getPostData(a,b,c):
    tempArr = [a,b,c]
    launderingList.append(tempArr)   
    