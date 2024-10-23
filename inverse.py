import numpy as np
a=int(input("Enter number of rows"))
b=int(input("Enter num of col:"))
matrix=[]
print("Entre entries")
for i in range(a):
 a=[]
 for j in range(b):
   a.append(int(input()))
 matrix.append(a)
print(matrix)
result=np.linalg.inv(matrix)
print(result)
