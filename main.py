from flask import Flask, render_template
import svm as sv
import decisionTree as dt
from RuleBased import RuleBasedAlertGeneration
import newDataset as dataset
import livedata as livedata
import json
import datetime
import requests
from flask import Flask, request, jsonify, render_template
from types import *

app = Flask(__name__)

allChatList = []
allChatDictionary = {}

@app.route('/mainAnalysis', methods = ['GET'])
def getMainAnalysisPage():
    print ("The result is : ", sv.retData())
    return render_template("analysis.html")

@app.route('/data', methods = ['GET'])
def getData():  
    return render_template("data.html")

@app.route('/visualization', methods = ['GET'])
def getDataVisualization():  
    return render_template("dataVisualization.html")

@app.route('/livedemo', methods = ['GET'])
def getLiveDemo():  
    return render_template("liveClassificationDemo.html")


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
    

@app.route('/ml', methods  = ['GET'])
def getMLData():
        a = sv.retData()
        return a
        #return sv.retData()

@app.route('/getdataML', methods  = ['GET'])
def getGraphMLAnalysisData():
        a = sv.retData()
        return a
    
@app.route('/getdataRuleBased', methods  = ['GET'])
def getGraphRuleBaedAnalysisData():
        rl = RuleBasedAlertGeneration()
           
        return rl.main() 

if __name__=="__main__"  :
    app.run(port=9040, debug=True)# -*- coding: utf-8 -*-
    #debug=True

