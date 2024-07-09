import numpy as np

arr = np.array([[10,20,30,40],[50,60,70,80],[20,40,60,80]])

print(arr)
print(type(arr))

#Multi dimensional slicing
print(arr[:2,:2]) # [[10 20] [50 60]]
print(arr[0,1:3]) # [20 30] - Array 0, [1:3]
print(arr[1,2:4]) # [70,80] -Array 1 [2:4]
print(arr[2,2]) # 60 -Array 2, 2nd element
print(arr[2,::-1])

#shape
print(np.shape(arr)) #(3,4)

#size - no. of elements
print(np.size(arr)) #3*4=12

#dimensions
print(np.ndim(arr)) #2-dimensional array

#datatype
print(arr.dtype)

#length
print(len(arr)) # 3 - rows


