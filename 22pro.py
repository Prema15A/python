#mano
from itertools import combinations
pxb,qgf=input().split()
qgf=int(qgf)
kxn=[]
cpm=len(pxb)-qgf
fakh=combinations(pxb,cpm)
for i in list(fakh):
kxn.append("".join(i))
print(min(kxn))
