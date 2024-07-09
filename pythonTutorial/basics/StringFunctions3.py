a = "Harry Potter"
print(a)

#endswith()
print(a.endswith('r'))
print(a.endswith('t',6,9))

#startswith()
print(a.startswith('H'))
print(a.startswith('P',6,9))

#swapcase()
print(a.swapcase())

#strip()
b = "     Harry Potter      "
print(b.strip()) #default means white space before & after string
c = "     *****Harry Potter   ....   "
print(c)
print(c.strip('*,., '))

#split()
d = "#OOFD#BRB#OMW#TB"
print(d.split("#"))
e = "hello. my name is john. i am 23 years old"
print(e.split("."))

#ljust()
print(a)
#x=a.ljust(20) # default spaces
x=a.ljust(20,'*')
print(x,"is my favourite movie")

#rjust()
print(a)
#x=a.rjust(20)
x=a.rjust(20,'*')
print(x,"is my favourite movie")

#replace()
f="my name is john. john likes to play football"
print(f.replace('john','lisa'))

#rindex()
g = "Harry potter and the prisoner of Azkaban"
print(g.rindex("prisoner"))
print(g.rindex("potter"))
print(g.rindex("Harry"))

#rfind()
print(g.rfind("prisoner"))
print(g.rfind("potter"))
print(g.rfind("Harry"))

h= "bibidy bobidy boo"
print(h.rfind("dy"))
print(h.rfind("dy",1,7))
print(h.rfind("dy",6,14))
print(h.rfind("dy",6,12)) # returns -ve value as it is close to left side or range is less than required