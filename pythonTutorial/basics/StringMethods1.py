a = "Harry Potter and the Goblet of Fire"
print(a)
print(type(a))

#len(): to find the length of the string
print(len(a))

#to find the no. of times a character is occuring
print(a.count('r'))
print(a.count('H'))
print(a.count('H'))

#to convert each letter into upper case
print(a.upper())

#to convert each letter into lower case
print(a.lower())

#to find the index of character
print("Index: ",a.index("o"))
print("Index of 2nd 'O': ",a.index("o",15,34))

#to find the index number of a character
print("find: ",a.find('o'))
print("find 2nd 'O': ",a.find('o',15,34))

#capitalize() : to convert first letter to capital
print(a.capitalize())

#to convert a string into lower case
print(a.casefold())

#format(): to write variables inside a string
name = "John"
age = 24
school = "UMSL"
#b= "my name is ", name #if u dont wanna represent as variable
#print(b)
b = "my name is {}, age: {} & my school is {}"
print(b.format(name,age,school))

#center(): It fills the given string & centralizes given string
print(name.center(20,'*'))


