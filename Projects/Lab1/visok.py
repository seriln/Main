import sys
try:
    year = float(raw_input("\nEnter a year: "))
except(ValueError):
    print "That was not a year!" 
else:
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
