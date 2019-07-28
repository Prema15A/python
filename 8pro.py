import math
prem,ser=map(int,input().split())
srww=[]
bob=list(map(int,input().split()))
for i in range(0,ser):
    lcc,hcc=map(int,input().split())
    srww.append([lcc,hcc])
for i in srww:
    din=i[0]-1
    eit=i[1]-1
    print(math.gcd(bob[din],bbb[eit]))
