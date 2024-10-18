#!/usr/bin/env python3

 #print(line, end="")
#this is how you read a file line by line you do the for line in file because if you just     tell it to read it will read the file once and get to the end and not do anything else.     As well as it uses alot of memory depending on how big your file is to read it all at onc    e so they tend to read things line by line.

import re

#Q1 took me 30 mins lol
file = open("Python_07_nobody.txt")

dn=0

for line in file:
  if "Nobody" in line:
    dn += 1
print(dn)

#Q2 substitute the occurance of 'Nobody" w fav name and write output file w persons name

renamefile = open("Python_07_Bob.txt","w")
file = open("Python_07_Nobody.txt","r")
for line in file:
  rename = re.sub(r'Nobody','Bob',line)
  print(rename,file=renamefile)






