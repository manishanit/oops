a=list()
b=list()
n=raw_input()
m=raw_input()
print n
print m
for i in range(1,(n+1)):
    a.append(i)
for i in range((n+1),((2*n)+1)):
    b.append(i)
c=dict()
for i in a:
    for j in b:
       c[i+j]=c.get((i+j),0)

print c
