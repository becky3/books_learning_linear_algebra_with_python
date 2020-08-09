import numpy as np
import matplotlib.pyplot as plt

N = 10000
path = '../resources/mnist'

with open(f'{path}/t10k-images.idx3-ubyte', 'rb') as f1:
    X = np.fromfile(f1, 'uint8', -1)[16:]
X = X.reshape((N, 28, 28))
with open(f'{path}/t10k-labels.idx1-ubyte', 'rb') as f2:
    Y = np.fromfile(f2, 'uint8', -1)[8:]
D = {y: [] for y in set(Y)}
for x, y in zip(X, Y):
    D[y].append(x)
print([len(D[y]) for y in sorted(D)])

fig, ax = plt.subplots(10, 10)
for y in D:
    for k in range(10):
        A = 255 - D[y][k]
        ax[y][k].imshow(A, 'gray')
        ax[y][k].tick_params(labelbottom=False, labelleft=False, color='white')

plt.show()
