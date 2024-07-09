A=["Ross","Rachel","Monica","Joe"]
## 1. Write a program to swap first &  forth element.
print("A: ",A)
A[0],A[3] = A[3],A[0]
print("After swap A: ",A)
##2. Write a prog to add a new value at second position.
A.insert(1,"Phoebe")
print("After adding at 2nd position: ",A)
##3. Write a prog to delete a value from 3rd position.
A.pop(2)
print("After pop at 3rd position: ",A)

B = [13,7,12,10]
##4. Write a prog to multiply all numbers in list.
mul = 1
for i in B:
    mul *= i
print("mul: ",mul)
##5. Write a prog to get the largest no. from list.
print("B: ", B)
#arrange list in ascending order
B.sort()
print("After sorting B: ", B)
print("Largest value in the list: ",B[-1])
##6.Write a prog to get the smallest no. from list.
print("Smallest value in the list: ",B[0])