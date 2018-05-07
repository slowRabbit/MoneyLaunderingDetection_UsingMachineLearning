from sklearn import tree
from flask import jsonify,  json
import getArray
from flask import Response


launderingList = []
normalList = []

#tempArr  = [0.0,105657.71,979014.18]
#launderingList.append(tempArr)
#tempArr  = [0.0,2250319.57,2931845.19]
#launderingList.append(tempArr)

def returnCasesList():

    
    print("launderingList :", launderingList)
    return jsonify({'Cases_List':
            {
                    'launderingList': launderingList,
                    }
        })
    
def getPostData(a,b,c):
    tempArr = [a,b,c]
    launderingList.append(tempArr)   
    