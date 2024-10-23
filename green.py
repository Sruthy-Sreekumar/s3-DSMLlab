import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,6,2,18])
y=np.array([3,12,10,20])
plt.plot(x,y)
plt.title("Line diagram")
plt.scatter(x,y,color="green")
plt.plot(x,y,linestyle="dotted",color="red")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
