import datetime

x = datetime.datetime.now()
print(x) #2024-06-27 02:03:33.475838
print(x.strftime("%M")) #minutes
print(x.strftime("%S")) #seconds
print(x.strftime("%p")) #AM/PM
print(x.strftime("%H")) #hour

y = datetime.datetime(1997,10,14)
print(y) #1997-10-14 00:00:00
print(y.strftime("%a")) #Tue
print(y.strftime("%A")) #Tuesday
print(y.strftime("%Y")) #1997
print(y.strftime("%y")) #97
print(y.strftime("%p")) #AM/PM
print(y.strftime("%S")) #seconds
print(y.strftime("%M")) #minutes

######################################################################

import random

a = random.randint(1,6) #example for dice
print(a) #It picks any random integer btw given range

l = ["Heads","Tails"]
b = random.choice(l)
print(b)
#########################################################################

import math

c = max(13,67,45)
print("Max value is ",c)

d = min(13,67,45,3,5)
print("Min value is ",d)

e = pow(4,3) #pow(base,exponent)
print(e)

f = math.sqrt(49)
print(f)

g = abs(-6.34*4)
print(g)

h = math.ceil(2.34)
print(h)

j = math.floor(2.34)
print(j)