import PIL.Image as Img
from numpy import array

im1 = Img.open('../resources/coast.jpg').convert('L')
im1.thumbnail((100, 100))
A = array(im1)
m, n = A.shape
B = A < 128
h = max(m, n)
y0, x0 = m/h, n/h

def f(i, j):
    return (y0 * (-1 + 2* j / (n-1)), x0 * (1-2*i / (m-1)))


P = [f(i, j) for i in range(m) for j in range(n) if B[i, j]]
with open('../resources/coast.txt', 'w') as fd:
    fd.write(repr(P))

