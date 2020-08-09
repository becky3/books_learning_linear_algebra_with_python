C = {'Earth': '3rd', 'Mars': '4th', 'Jupiter': '5th'}
for x in C:
    print(f'{x} is the {C[x]} planet in the solar system.')
print()
for x in sorted(C):
    print(f'{x} is the {C[x]} planet in the solar system.')
    
