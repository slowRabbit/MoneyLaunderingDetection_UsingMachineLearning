# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:01:17 2018

@author: prashant
"""

class RuleBasedAlertGeneration:
    
    def main(self):
        print("hello")
        totalTrans= 0 
        falsePositiveTrans= 0
        
        
        # file-input.py
        f = open('/media/cyris/Studies/Hackathons/CodeGrind17/Data set/TestingDataSets/generated_DS_TRAIN_RULE_A.txt','r')
        message = f.read()
        #print(message)
    
        
        data1 = message.split("\n")
        print ("Data 1 is : ", data1)
        for temp in data1[:-1]:
            
            
            bIsAlert=False 
            totalTrans=totalTrans + 1
            print(totalTrans)
            data = temp.split(",")
            print("Data is : ", data)
            
            
            #break;
            str1AccType= data[0]
            str2TransType=data[1]
            f3Amount=float(data[2])
            str4Month= data[3]
            str5TransTiming=data[4]
            str6LocationRisk=data[5]
            avgTransactions=data[6]
            bOriginal=bool(data[7])
            
            
            
            if f3Amount > 75000 :
                print("inside f3")
                bIsAlert=True
            
            if str2TransType is "cash-out" :
                print("str2TransType")
                bIsAlert=True
            
            if str6LocationRisk is "high" :
                print("str6LocationRisk")
                bIsAlert=True
            
            print("sjgdvsa",bIsAlert)
            if bIsAlert != bOriginal:
                falsePositiveTrans = falsePositiveTrans +1
            
            print(data,", classified as :",bIsAlert)
        
        print("Total transaction are",totalTrans)
        print("False transaction are:",falsePositiveTrans)
        efficiency = (falsePositiveTrans*100)/totalTrans 
        print("efficiency",efficiency)
    
rl = RuleBasedAlertGeneration()
rl.main()     
print("djsavd" + "heaf")  
print("Total transaction are")
        
        