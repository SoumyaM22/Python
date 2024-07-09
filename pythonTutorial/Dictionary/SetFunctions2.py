a = {"Spiderman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-woman"}
c = {"Hulk","Thor"}
d = {"Ironman","Hulk","Thor","Captain America"}
e = {"Hulk","Thor","Spiderman"}

#isdisjoint()
print(a.isdisjoint(b))
print(a.isdisjoint(c))
#issubset()
print(c.issubset(a))
#issuperset()
print(a.issuperset(b))
#update()
x = a.update(b)
print(x)
y = d.update(e)
print(y)
#clear()
a.clear()
print(a)

#Union
print(d.union(e))

#difference
#print(d.difference(e))
x = d.difference(e)
print(x)
#difference_update
d.difference_update(e)
print(d)

#Intersection
A = {1,2,3}
B = {3,4,5}

print(A.intersection(B))

#Intersection update
A.intersection_update(B)
print(A)

#Symmetric Difference
z = A.symmetric_difference(B)
print(z)

#Symmetric Difference Update
A.symmetric_difference_update(B)
print(A)




