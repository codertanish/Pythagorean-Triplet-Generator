import random
triplets = []
for i in range (1,25):
    m = i+1
    n = i
    a = abs(m**2 - n**2)
    b = 2*m*n
    c = m**2 + n**2
    triplets.append((a,b,c))
for i in range (1,25):
    m = i+3
    n = i
    a = abs(m**2 - n**2)
    b = 2*m*n
    c = m**2 + n**2
    triplets.append((a,b,c))
for i in range (1,25):
    m = i+5
    n = i
    a = abs(m**2 - n**2)
    b = 2*m*n
    c = m**2 + n**2
    triplets.append((a,b,c))
print(triplets)