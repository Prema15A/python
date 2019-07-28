ser=int(input())
cine=list(map(int,input().split()))
sws=[1]*ser
for i in range(ser):
    if i==0:
        if cine[i]>cine[i+1]:
            sws[i]=sws[i]+sws[i+1]
    elif i>0:
        if cine[i]>cine[i-1]:
            sws[i]=sws[i]+sws[i-1]
print(sum(sws))
