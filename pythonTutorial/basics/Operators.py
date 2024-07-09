#Arithmetic operators
print("(% )",8%3) # (%)-> Remainder
print("(// )",8//2) # (//)-> Quotient
print("(**)",2**10) # (**)-> Exponent

#Comparison Operators
print(3<6)
print(6<3)
print(3==6)
print(3==3)
print(3!=6)
print(3!=3)

#Logical Operators
print(not(3>4 and 3<4))

#Assignment operators
x=6
print(x)
x+=2
print(x)
x-=2
print(x)
x*=2
print(x)

#Identity operators
a=1234
b=1234
c="1234"

print(a is b)
print(a is not c)

#Bitwise Operators
print(bin(15))
a=10
b=8
print("a&b: ",a&b)
print("a|b: ",a|b)
print("a^b: ",a^b)
print("a>>2: ",a>>2)
print("a>>1: ",a>>1)
print("a<<2: ",a<<2)
print("a<<1: ",a<<1)

#Membership Operators
a="hello"

print("p in a: ","p" in a)
print("p not in a: ","p" not in a)
print("o in a: ","o" in a)
