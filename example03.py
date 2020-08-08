import sympy
from sympy.abc import x,y

ans1 = sympy.solve([x +2*y -1, 4*x +5*y -2])
print(ans1)
ans2 = sympy.solve([x**2 +x +1])
print(ans2)
ans3 = sympy.solve([x**2 +y**2 -1, x -y])
print(ans3)
