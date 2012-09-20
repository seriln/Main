import math
import sys
i = sys.argv[1]
j = int(sys.argv[2])
if i == "pi":
    print round(math.pi,j)
elif i == "e":
    print round(math.e,j)

