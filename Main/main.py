from flask import Flask, render_template

app = Flask(__name__)

allChatList = []
allChatDictionary = {}

@app.route('/moneyTracker', methods = ['GET'])
def getMainPage():
    return render_template("sample.html")

@app.route('/data', methods = ['GET'])
def getData():
    return render_template("data.html")

if __name__=="__main__"  :
    app.run(port=8040, debug=True)# -*- coding: utf-8 -*-
    #debug=True

