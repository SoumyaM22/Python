## Iteration using For loop
a = ["Hulk","Thor","Ironman","Captain America"]
#for i in a:
#    print(i)
## Iteration using for loop with Range & length function
#print("length: ",len(a))
#for i in range(len(a)):
#    print(a[i])
## Iteration using while loop (indexing)
i=0
while i<len(a):
    print(a[i])
    i +=1
print("##############")
# Using Short-hand for loop
[print (i) for i in a]