#1. Write a python program to sort a dictionary by value.
a= {"a":12,"b":56,"c":6,"d":91,"e":45}
a=sorted(a.values())
print(a)
#2. Write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.
a={}
for i in range(1,16):
    a[i]=i**2
print(a)
#3. Write a program to multiply all the items in a dictionary.
a= {"a":1,"b":2,"c":3,"d":4,"e":5}
product = 1
for i in a:
    product *= a[i]
print(product)
#4. Write a python program to sort a dictionary by key.
a= {12:"a",56:"b",6:"c",91:"d",45:"e"}
a=sorted(a.keys())
print(a)