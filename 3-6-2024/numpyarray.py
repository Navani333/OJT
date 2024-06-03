import numpy as np

#create an array with 1-d array
array_1D= np.array([1,2,3,4,5])
print("1D Array :",array_1D)


#2D
array_2D = np.array([[1,2,3],[4,5,6]])
print("2D Array :",array_2D)

#3D
array_3D = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print("3D Array :",array_3D)

#create an array with ones
array_ones =np.ones((2,4))
print("Array with ones : ",array_ones)

#create an array with zeros
array_zeros=np.zeros((3,3))
print("Array with zeros :",array_zeros)

#create an array with a particular range
array_range=np.arange(10)
print("array with range : ",array_range)