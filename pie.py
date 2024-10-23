import matplotlib.pyplot as plt
languages="Java","python","php","javascript","c#","c++"
popularity=[22.2,17.6,8.8,8,7.7,6.7]
colors=["blue","green","black","red","orange","yellow"]
plt.pie(popularity,labels=languages,colors=colors)
plt.axis('equal')
plt.show()
