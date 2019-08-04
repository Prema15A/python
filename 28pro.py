bgn=int(input())
npk=list(map(int,input().split()))
npk.sort()
syn=0
sps=0
for i in range(len(npk)):
    if npk[i]>=syn:
        sps=sps+1
    syn=syn+npk[i]
print(sps)
