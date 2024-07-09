#1. Write a program to find max & min in a set.
a = {12,56,34,8,90,1,57}
maximum = max(a)
minimum = min(a)
print("the maximum value of set a: ", maximum)
print("the minimum value of set a: ", minimum)

#2. Write a program to find common elements in 3 lists using sets.
a = [1,5,6,8,2]
b = [4,5,6,7]
c = [1,9,6,2,5]

print("The common elements in the given 3 lists are: ",set(a) & set(b) & set(c))

#3. Write aprogram to find difference between 2 sets.
a = {1,5,6,8,2}
b = {1,9,6,2,5}
print(b.difference(a))

#4. Write a python prog to remove an item from a set if it is present in the set.
a = {1,5,6,8,2}
a.discard(6)
print(a)
#a.discard(12) #It wont delete this element, if it doesn't contain it
#print(a)

#5. Write a program to check if a set is subset of another set.
c = {1,5,6,2}
d = {1,9,6,2,5}
print(c.issubset(d))