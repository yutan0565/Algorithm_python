import sys
import math

r = int(sys.stdin.readline().rstrip())


print("{:5f}".format(round((r**2)*math.pi, 6)))
print("{:6f}".format(round( (r*(2**(0.5))) **2,6)))