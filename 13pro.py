aoa,bob=map(int,input().split())
cat=[]
sim=[]
prem=[int(m) for m in input().split() ]
for i in range(0,bob):
    uu1,vv1=map(int,input().split())
    for j in range(uu1-1 ,vv1):
        sim.append(prem[j])
    mah=sorted(sim)
    cat.append(min(sim))
    del sim[:]
for z in range(0,len(cat)):
    print(cat[z])
