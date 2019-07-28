import math
prem,sup=map(int,input().split())
smi=[]
ber=list(map(int,input().split()))
for i in range(0,sup):
    loc,hoc=map(int,input().split())
    smi.append([loc,hoc])
for i in smi:
    don=i[0]-1
    eot=i[1]-1
    print(math.gcd(ber[don],ber[eot]))
