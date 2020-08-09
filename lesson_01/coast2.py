import matplotlib.pyplot as plt

with open('../resources/coast.txt', 'r') as fd:
    P = eval(fd.read())
x, y = zip(*P)
plt.scatter(x, y, s=5)
plt.axis('scaled')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()
