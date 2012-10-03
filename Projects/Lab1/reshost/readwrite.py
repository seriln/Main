import os
import string

dir = os.getcwd()
l = len(open('hosts.txt','r').readlines())
dict = {}

filehandle = open('hosts.txt', 'r')
for items in filehandle:
    k = items[:string.find(items,' ')]
    v = items[string.find(items,' ')+1:]
    dict[k]=v
filehandle.close()

for items in dict:
    print items +'\t\t' +dict[items]

while 1:
    vetka = str(raw_input("\nAdd new host? (y/n):"))
    if string.lower(vetka) == 'y':
        newrow = str(raw_input("\nEnter new row (address hostname): "))
        if string.find(newrow,' ') == -1:
            print "Incorrect name"
            break
        k = newrow[:string.find(newrow,' ')]
        v = newrow[string.find(newrow,' ')+1:]
        print k , v
        fh = open('hosts.txt', 'a')
        fh.write(k+' '+v+'\n')
        fh.close()
        break
    elif string.lower(vetka) == 'n':
        break
    
