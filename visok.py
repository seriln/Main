import sys
year = int(sys.argv[1])
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print "visocosniy"
        else:
            print "ne visocosniy"
    else:
        print "visocosniy"
else:
    print "ne visocosniy"
