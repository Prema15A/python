prem=input()
yan=map(int,input().split())
sun=[]
for i in yan:
    eats=bin(i)
    sun.append(eats)
fines=sorted(sun)
fines.reverse()
for j in fines:
    print(int(j,2))
