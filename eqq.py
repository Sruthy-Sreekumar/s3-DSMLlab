import numpy as np
arr1=[1,2]
arr2=[1,2]
print("First array:",arr1)
print("Second array:",arr2)
if np.array_equal(arr1,arr2):
	print("Arrays are equal")
else:
	print("Arrays are not equal")
