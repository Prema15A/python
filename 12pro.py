prem,suop=map(int,input().split())
last=list(map(int,input().split()))
line=[]
for i in range(0,suop):
     xp,yq=map(int,input().split())
     line.append([xp,yq])
for i in range(suop):
     lowers=line[i][0]
     uppers=line[i][1]
     samu=sum(last[lowers-1:uppers])
     print(samu)
