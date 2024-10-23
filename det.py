import numpy as np
a=int(input("Enter number of rows"))
b=int(input("Enter num of col:"))
print("Entre entries")
matrix=[]
for i in range(a):
 a=[]
 for j in range(b):
   a.append(int(input()))
 matrix.append(a)
print(matrix)
result=np.linalg.det(matrix)
print(result)
