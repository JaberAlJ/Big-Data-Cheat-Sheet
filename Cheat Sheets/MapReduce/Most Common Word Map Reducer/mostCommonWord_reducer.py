#!/usr/bin/python

import sys

dict1={}				
firstTime = "true"				

for line in sys.stdin:
  word,count=line.split(',')		
  if(firstTime=="true"):				
    dict1[word]=int(count)		
    firstTime="false"


  wordExist=[key for key in dict1]	
  if(word in wordExist):
    dict1[word]=dict1[word]+int(count)	 
  else:
    dict1[word]=int(count)		


maximum=max(dict1,key=dict1.get)
print(maximum,dict1[maximum])
