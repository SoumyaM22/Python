a = ("Oneplus", "Vivo","Redmi","Samsung","Nokia")
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[::2])
print(a[::-1])
print(a[2::-1])
print(a[1::2])

#with for loop
print("*******For loop*******")
for i in a:
    print(i)

print("*******For loop along with range & length*******")
for i in range(len(a)):
    print(a[i])
len(a)
print("*******While loop*******")
i=0
while i<len(a):
    print(a[i])
    i += 1
