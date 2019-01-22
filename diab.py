#!/usr/bin/env python3
print("Content-Type:text/html")
print("")

import cgi

import pandas as pd
import  seaborn  as  sb
from  sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import cgitb   #cgitb to trace back error
cgitb.enable()
#this is http protocol model'
web=cgi.FieldStorage()
a=web.getvalue("Preg")
b=web.getvalue("glu")
c=web.getvalue("bp")
d=web.getvalue("ST")
e=web.getvalue("Insu")
f=web.getvalue("bmi")
g=web.getvalue("DPF")
h=web.getvalue("age")
#print([a,b,c,d,e,f,g,h])
print("-----------------------------------------------")

#print("Hello")

#  reading csv file and converting into data frames
df=pd.read_csv('/usr/lib/cgi-bin/diabetes.csv')
#df.head(5) this wil, display first 5 rows of dataset

#  creating  training and testing datasets 
diabetes_target=df['Outcome']  # df['outcome'] gives all output means complete labels of dataset

diabetes_data=df[df.columns[:-1]]   # df[df.colums[:-1]] gives all features of complete dataset 

#sb.countplot(df['Outcome']) countplot function of seaborn which count total of different outcome or other feature

#df.info()   to check all info about  data with null values

#df.hist(figsize=(14,14)) this will display histogram of all features

#df.groupby('Outcome').size()  group different values of outcome feature and size print total value

#spliting dataset
split_data=train_test_split(diabetes_data,diabetes_target,test_size=0.1)

train_data,test_data,train_target,test_target=split_data

#implementing decision tree classifier
dsc_algo=DecisionTreeClassifier()

#print(test_data)

trained_dsc=dsc_algo.fit(train_data,train_target)
#print (trained_dsc)
var = [[a,b,c,d,e,f,g,h]]
output_dsc=trained_dsc.predict(var)


#print (test_target)
#print (output_dsc)
if output_dsc=='1':
	print("Yes you are diabetic")
else:
	print('No you are not diabetic')
#to check accuracy score
#acc_dsc=accuracy_score(test_target,output_dsc)
#print("Accuracy score using Decision Tree Classifier:",acc_dsc)


