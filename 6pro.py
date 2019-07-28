prem1=int(input())
prem2=list(map(int,input().split()))
ants=0
for x in range(len(prem2)-2):
    for y in range(x+1,len(prem2)-1):
        for z in range(y+1,len(prem2)):
            if prem2[x]<prem2[y]<prem2[z] and x<y<z:
                ants=ants+1
print(ants)
