import math
i = str(raw_input("\nEnter a constant: "))
try:
    j = int(raw_input("\nEnter a accuracy: "))
except(ValueError):
    print "Accuracy wrong"
else:
    if i == "pi":
        print round(math.pi,j)
    elif i == "e":
        print round(math.e,j)
    else:
        print "Constant does not exist"

