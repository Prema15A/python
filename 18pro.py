prem,ser=map(int,input().split())
srk=[]
til=0
for i in range(prem):
    srk.append(list(map(int,input().split())))   
for i in range(prem):
    for j in range(ser-1):
        for k in range(j+1,ser+1):
            if srk[i][j:k]==[1]*len(srk[i][j:k]):
                 if all(srk[p+i][j:k]==[1]*len(srk[p+i][j:k]) for p in range(len(srk[i][j:k])-1)):
                     if len(srk[i][j:k])>til:
                        til=len(srk[i][j:k])
if len(srk)==1 and len(srk[0])==1 and srk[0][0]==1:
    print(1)
for i in range(til):
    print(*[1]*til)
