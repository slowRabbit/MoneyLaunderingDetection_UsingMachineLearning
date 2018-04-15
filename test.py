#import module1 as m1

print("----------------Dictionary -----------------\n")

besties = [['Prashant':'chindi'], obama':'mindless', 'shivani':'vicco bajridanti']

print(besties['obama'])

for k, v in besties.items():
    print(k, "-", v)


print("----------------Modules -----------------\n")

#a=m1.multiply(5,2)
#print (" 5 multiply by 2 is ", a)



print("----------------Read/Write Files -----------------\n")

fw= open('sample.txt', 'w')
fw.write('this is the first file i am writing \n')
fw.write('this it the second line in it sytem')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()# -*- coding: utf-8 -*-

