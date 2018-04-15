from flask import Flask, render_template

app = Flask(__name__)

allChatList = []
allChatDictionary = {}

@app.route('/mainAnalysis', methods = ['GET'])
def getMainAnalysisPage():
    return render_template("analysis.html")

@app.route('/data', methods = ['GET'])
def getData():  
    return render_template("data.html")

if __name__=="__main__"  :
    app.run(port=8040, debug=True)# -*- coding: utf-8 -*-
    #debug=True

