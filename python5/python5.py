#!/usr/bin/env python3

fav_dict = { 'book' : 'STEP1', 'flower' : 'poppy', 'tree' : 'willow'}

#print fav book
print(fav_dict['book'])

#print fav book using variable in key
fav_thing = 'book'
print(fav_dict[fav_thing])

print(fav_dict['tree'])

fav_dict['organism'] = 'humans'
print(fav_dict) 

#use loop to print out each key and value of dictionary
for fav in fav_dict:
  print (fav, fav_dict[fav])

#input problem
x = input("pick a favorite thing: ")
print(fav_dict[x])

#9 change value of organism
fav_dict['flower'] = 'rose'
print(fav_dict['flower'])

#10 get fav thing from command line




