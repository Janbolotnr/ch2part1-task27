import random

n = []
for i in range(10):
    n.append(int(random.random() * 10) - 5)
print(n)    

neg = []
pos = []

for i in n:
    if i < 0:
        neg.append(i)
    elif i > 0:
        pos.append(i)

print(neg)
print(pos)            
        