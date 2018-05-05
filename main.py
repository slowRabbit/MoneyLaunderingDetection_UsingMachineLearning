from flask import Flask, render_template
import svm as sv
import decisionTree as dt
from RuleBased import RuleBasedAlertGeneration

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
    app.run(port=8040, debug=True)# -*- coding: utf-8 -*-
    #debug=True

