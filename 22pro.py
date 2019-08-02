syr=int(input())
bzh=list(map(int,input().split()))[:syr]
zq=sum(bzh[0:syr:2])
ywk=sum(bzh[1:syr:2])
if zq>ywk:
  print(zq)
else:
  print(ywk)
