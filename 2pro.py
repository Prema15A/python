#mano
from itertools import combinations
paw,qiz=input().split()
qiz=int(qiz)
kqh=[]
com=len(paw)-qiz
far=combinations(paw,com)
for i in list(far):
  kqh.append("".join(i))
print(min(kqh))
