import matplotlib.pyplot as plt
languages="Java","python","php","javascript","c#","c++"
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(languages,popularity,color="blue")
plt.xlabel("languages")
plt.ylabel("popularity")
plt.show()
