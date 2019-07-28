prem,mkh=map(int,input().split())
lists1=list(map(int,input().split()))
prem=[]
lists1.insert(0,0)
for y in range(mkh):
     van=[]
     ss=0
     bob,zoz=map(int,input().split())
     for i in range(bob,zoz+1):         
         ss^=lists1[i]     
     prem.append(ss)
for y in prem:
     print(y)
