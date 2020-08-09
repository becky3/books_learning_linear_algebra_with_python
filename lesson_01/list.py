import sys

def p(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
      print(objects, sep=sep, end=end, file=file, flush=flush)

B = ['Earth','Mars','Jupiter']
print(B)

p(B[0], B[1], B[2])
p(B[-1], B[-2], B[-3])
B.append('Saturn')
p(B)
