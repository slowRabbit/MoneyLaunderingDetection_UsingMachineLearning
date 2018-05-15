from flask import Flask, render_template
import svm as sv
import decisionTree as dt
from RuleBased import RuleBasedAlertGeneration
#import newDataset as dataset
import livedata as livedata
import json
import datetime
import requests
from flask import Flask, request, jsonify, render_template
from types import *

app = Flask(__name__)

allChatList = []
allChatDictionary = {}

@app.route('/overview', methods = ['GET'])
def getMainToolPage():  
    return render_template("a_overView.html")

@app.route('/mainAnalysis', methods = ['GET'])
def getMainAnalysisPage():
    print ("The result is : ", sv.retData())
    return render_template("analysis.html")

@app.route('/analysis', methods = ['GET'])
def getAnalysisPage():
    print ("The result is : ", sv.retData())
    return render_template("c_analysis.html")

@app.route('/data', methods = ['GET'])
def getData():  
    return render_template("data.html")

@app.route('/livedemo', methods = ['GET'])
def getLiveDemo():  
    return render_template("d_liveDemo.html")

#@app.route('/visualization', methods = ['GET'])
#def getDataVisualization():  
#   return render_template("dataVisualization.html")

@app.route('/visualization', methods = ['GET'])
def getDataVisualization2():  
    return render_template("b_data.html")

@app.route('/roundgraph', methods = ['GET'])
def getRoundGraphForComparision():  
    return render_template("round.html")



@app.route('/getLiveData', methods = ['GET'])
def getLiveDataforLiveDemo3DGraph():
    data = livedata.returnCasesList()
    return data

@app.route('/postLiveData', methods =['POST'])
def postLiveDataforLiveDemo3DGraph():
    response = request.get_json()
    a = response.get("a")
    b = response.get("b")
    c = response.get("c")
    livedata.getPostData(a,b,c)
    print(a,b,c)
    return "thank you"
    

#@app.route('/ml', methods  = ['GET'])
#def getMLData():
#        a = sv.retData()
#        return a
        #return sv.retData()

#@app.route('/getdataML', methods  = ['GET'])
#def getGraphMLAnalysisData():
#        a = sv.retData()
#        return a
    
#@app.route('/getdataRuleBased', methods  = ['GET'])
#def getGraphRuleBaedAnalysisData():
#        rl = RuleBasedAlertGeneration()
           
#        return rl.main() 

if __name__=="__main__"  :
    print("server started !")
    app.run(port=7040, debug=True)# -*- coding: utf-8 -*-
    #debug=True

