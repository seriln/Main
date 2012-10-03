import os
import string

dict = {}
while 1:
    vetka = str(raw_input("\nSearch by address or by hostname? (a/h/q): "))
    if string.lower(vetka)=='a':
        filehandle = open('hosts.txt', 'r')
        for items in filehandle:
            k = items[:string.find(items,' ')]
            v = items[string.find(items,' ')+1:]
            dict[k]=v
        filehandle.close()
        address = str(raw_input("\nEnter an address: "))
        print dict[address]
        break
    elif string.lower(vetka)=='h':
        filehandle = open('hosts.txt', 'r')
        for items in filehandle:
            k = items[:string.find(items,' ')]
            v = items[string.find(items,' ')+1:]
            dict[v]=k
        filehandle.close()
        hostname = str(raw_input("\nEnter an hostname: "))
        print dict[hostname+'\n']
        break
    if string.lower(vetka)=='q':
        break


