import matplotlib.pyplot as plt
x=[i for i in range(1,5)]
y=[i for i in range(1,9,2)]
c=[i for i in "gyrb"]
plt.bar(x,y,color=c)
plt.show()