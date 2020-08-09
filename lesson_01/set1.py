A = {2, 3, 5, 7}
print(A)

B = {3, 6, 9, 6, 3};
print(B)

print(set())

print(f"B == {3, 6, 9} : {B == {3,6,9}}")
print(f"2 in A：{2 in A}")
print(f"2 in B：{2 in B}")
print(f"A | B：{A | B}")
print(f"A & B：{A & B}")
print(f"(A & B).issubset(A)：{(A & B).issubset(A)}")
print(f"A.issubset(A | B)：{A.issubset(A | B)}")
print(f"A | B == A.union(B)：{A | B == A.union(B)}")
print(f"A & B == A.intersection(B)：{A & B == A.intersection(B)}")
