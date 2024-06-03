import numpy as np

array_2D = np.array([[1,2,3], #0
                     
                     [4,5,6]]) #1

#ascending a single element
element =array_2D[1,2]
print("element at the index of [1,2]",element)

element =array_2D[0,1]
print("element at the index of [0,1]",element)

#access by 2 row
row=array_2D[1:]
print("second row",row)

column=array_2D[:,1]
print("element at the index of [0,1]",column)

#slicing
slice_array=array_2D[0:2,1:3]
print("subarray",slice_array)