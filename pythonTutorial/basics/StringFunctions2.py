a = "hello"
b = "Hello123"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123"
g = "1.234"
h = "Harry Potter And The Goblet Of Fire"
j= "HELLO everyone"
#isalnum(): allows alpha / numeric
print("**********isalnum(): ******************")
print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalnum())
print(d,d.isalnum())
print(e,e.isalnum())
print(f,f.isalnum())
print(g,g.isalnum())

#isalpha()
print("************isalpha(): ****************")
print(a, a.isalpha())
print(b, b.isalpha())
print(c, c.isalpha())
print(d, d.isalpha())
print(e, e.isalpha())
print(f, f.isalpha())
print(g, g.isalpha())

#isdecimal(): allows integers but not float
print("************isdecimal(): ****************")
#print(a, a.isdecimal())
#print(b, b.isdecimal())
print(c, c.isdecimal())
#print(d, d.isdecimal())
#print(e)
#print(f)
print(g, g.isdecimal())

#isdigit():
print("************isdigit(): ****************")
print(a, a.isdigit())
print(b, b.isdigit())
print(c, c.isdigit())
#print(d)
#print(e)
print(f, f.isdigit())
print(g, g.isdigit())

#isnumeric():
print("************isnumeric(): ****************")
#print(a)
print(b, b.isnumeric())
print(c, c.isnumeric())
print(d, d.isnumeric())
print(e, e.isnumeric())
print(f, f.isnumeric())
print(g, g.isnumeric())

#islower()
print("************islower(): ****************")
print(a, a.islower())
print(b, b.islower())
#print(c)
print(d, d.islower())
print(e, e.islower())
print(f, f.islower())
#print(g)

#isupper()
print("************isupper(): ****************")
print(a, a.isupper())
print(b, b.isupper())
#print(c)
print(d, d.isupper())
print(e, e.isupper())
print(f, f.isupper())
#print(g)

#isspace()
print("************isspace(): ****************")
#print(a,)
#print(b)
#print(c)
#print(d)
print(e, e.isspace())
print(f, f.isspace())
#print(g)

#istitle()
print("************istitle(): ****************")
print(f, f.istitle())
print(h, h.istitle())
print(j, j.istitle())