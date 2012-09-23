try:
    mon = str(raw_input("\nEnter a month: "))
except(ValueError):
    print "That was not a month!" 
else:
    dict = {'January':1, 
        'February':2,
        'March':3,
        'April':4,
        'May':5,
        'June':6,
        'July':7,
        'August':8,
        'September':9,
        'October':10,
        'November':11,
        'December':10}
    for key in dict:
        if key == mon:
            print dict[key]
            break
    else:
        print "That was not a month!"
