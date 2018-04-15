from flask import Flask, render_template
import svm as sv

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
    return sv.retData()

if __name__=="__main__"  :
    app.run(port=9040, debug=True)# -*- coding: utf-8 -*-
    #debug=True

