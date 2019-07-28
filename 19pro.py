bin=int(input())
prem=[]
moh=[]
for i in range(bin):
    prem.append(list(map(int,input().split())))
for sur in prem:
    for num in sur:
        moh.append(num)
moh.sort()
for i in moh:
    print(i,end=' ')
