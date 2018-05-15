# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:01:17 2018

@author: prashant
"""

from flask import Response
from flask import jsonify,  json

class RuleBasedAlertGeneration:
    
    
    
    def main(self):
        print("hello")
        totalTrans= 0 
        falsePositiveTrans= 0
        
        
        # file-input.py
        f = open('D:\Hackathons\CodeGrind17\Techfest April 17th\Datasets\data_for_rule_based_string.txt','r')
        message = f.read()
        #print(message)
    
        allLabelList = []
        positiveCaseList = []
        negetiveCaseList =[]
        ct_personal = 0
        ct_government = 0
        ct_corporate = 0
        ct_private = 0
        ct_ngo =0
        i = 0
        
        data1 = message.split("\n")
        #print ("Data 1 is : ", data1)
        for temp in data1[:-1]:
            i+=1
            
            
            bIsAlert=False 
            totalTrans=totalTrans + 1
            #print(totalTrans)
            data = temp.split(",")
            #print("Data is : ", data)
            
            
            #break;
            str1AccType= data[0]
            str2TransType=data[1]
            f3Amount=float(data[2])
            str4Month= data[3]
            str5TransTiming=data[4]
            str6LocationRisk=data[5]
            avgTransactions=data[6]
            bOriginal=bool(data[7])
            sOriginal=data[7]
       
            
            if sOriginal is "true":
                if str1AccType  is "personal":
                    ct_personal +=1
                elif str1AccType  is "corporate":
                    ct_corporate +=1
                elif str1AccType  is "govt":
                    ct_government +=1
                elif str1AccType  is "private":
                    ct_private +=1
                elif str1AccType  is "ngo":
                    ct_ngo +=1
                    
                    
            
            
            if f3Amount > 75000 :
                #print("inside f3")
                bIsAlert=True
            
            if str2TransType is "cash-out" :
                #print("str2TransType")
                bIsAlert=True
            
            if str6LocationRisk is "high" :
                #print("str6LocationRisk")
                bIsAlert=True
            
            #print("sjgdvsa",bIsAlert)
            allLabelList.append(i)
            if bIsAlert != bOriginal:
                #means a case of false negetive 
                falsePositiveTrans = falsePositiveTrans +1
                positiveCaseList.append(" ")
                negetiveCaseList.append("-1")
                
                
                
            else :
                positiveCaseList.append("1")
                negetiveCaseList.append(" ")
                
            
            #print(data,", classified as :",bIsAlert)
        
        print("Total transaction are",totalTrans)
        print("False transaction are:",falsePositiveTrans)
        efficiency = (falsePositiveTrans*100)/totalTrans 
        efficiency = 100-efficiency
        print("efficiency",efficiency)
        
        dict1 = {"efficiency": efficiency, "allLabelList": allLabelList[:40],"positiveCaseList": positiveCaseList[:40] ,
                 "negetiveCaseList": negetiveCaseList[:40], "personal":ct_personal, "corporate":ct_corporate, "govt":ct_government, "private":ct_private, "ngo":ct_ngo, }
        return Response(json.dumps(dict1), mimetype='application/json')
    
rl = RuleBasedAlertGeneration()
rl.main()     
print("djsavd" + "heaf")  
print("Total transaction are")
        
        