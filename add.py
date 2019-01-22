#!usr/bin/env python
import cgi   #to receive data from web server common gateway interface 

print("Content-type:text/html") #to store only html code and output of html
print("")# to ignore other details which we get from web server

web_data=cgi.FieldStorage()# store complete data of html page

#extracting variables from html page
x=web_data.getvalue('n1')
y=web_data.getvalue('n2')
print(x+y)
