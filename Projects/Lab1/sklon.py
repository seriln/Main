# -*- coding: utf-8 -*-
dict = {'1':'час', '2':'часа', '3': 'часа', '4':'часа','5':'часов',
        '6':'часов', '7':'часов', '8':'часов','9':'часов', '0':'часов' }

def humanizer(num,dict):
    for key in dict:
        if key == str(num)[len(str(num))-1]:
            print str(num)+" "+ dict[key]

try:
    num = int(raw_input("\nEnter a number: "))
except(ValueError):
    print "That was not a number!" 
else:
    humanizer(num,dict)
