c = open('commons.py')
b = open('blabla.py')
o = open('commons2.py', 'w')

u = [line.strip('\n') for line in c]
lo = [line for line in b]

for x, y in zip(u, lo):
    o.write(x + y)
