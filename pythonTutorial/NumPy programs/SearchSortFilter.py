import numpy as np

ar = np.array([[7,8,4,12,9],[2,8,5,1,3]])
print(np.sort(ar)) # sort an array

ar2 = np.array([3,4,1,7,8])
s1 = np.where(ar2 == 7) # to search an element
s2 = np.where(ar2 % 2 == 0)
print("search index of 7",s1)
print("search indexes of element divisible by 2",s2)

ar3 = np.array([1,2,3,4,5]) # here elements need to be sorted
ss = np.searchsorted(ar3,5)
print("Search sorted element index 5: ",ss)

###Filter#######
ar4 = np.array([20,30,40,50])
fa1 = [True, False, True, False] #filter - if u want index- 0,2 to be printed
# Where u need to retrieve values keep true
new1 = ar4[fa1] #pass filter to array
print(new1)

fa2 = ar4>35
new2 = ar4[fa2]
print(new2)

ar5 = np.array([2,3,4,5])
fa3 = ar5%2==0 # to get even no.s
new3 = ar5[fa3]
print(new3)
