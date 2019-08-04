nct = int(input())
lsa = list(map(int, input().split()))
maximum = 0
cpc = 0
aky = lsa[0]
for i in range(0,nct-1):
    if aky < lsa[i+1]:
        cpc +=1
        aky = lsa[i+1]
    else:
        if max(lsa[i+1:]) < aky:
            aky = lsa[i+1]
print(cpc+1)
