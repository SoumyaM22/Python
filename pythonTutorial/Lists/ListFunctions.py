a= ["Thor","Hulk","Ironman","Captain America","Hulk"]
# to find the length of list
print(len(a))

# to count occurance of a particular event
print(a.count("Hulk"))

# to add to the list
a.append("Spiderman") # adds at the end
print(a)

# to add to a specific location
a.insert(3,"Vision") # adds at index
print(a)

# to remove from a list
a.remove("Hulk") # 1st Hulk is removed
print(a)

# to remove from a certain location
a.pop(2)
print(a)

#######ListFunctions2#############################
##1. to create a copy of a list
b=[]
print(b)
b = a.copy()
print(b)
##2. to access an element
print("index of hulk: ",a.index('Hulk'))
a.pop(4)
print(a)
##3. to extend the list
#a.extend("Vision")
c=["Vision","Spiderman"]
a.extend(c)
print(a)

##4. reverse the list
a.reverse()
print(a)

##5. to sort the list
a.sort()
print(a)
d = [1,6,9,3,7,4,12]
d.sort()
print(d)
##6. to clear all the data from the list
d.clear()
print(d)

