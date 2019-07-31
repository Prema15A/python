prems=int(input())
maxm=list(map(int,input().split()))
anse=int(prems/2)
rtn=maxm[:anse]
mkn=maxm[anse::]
if ((sum(rtn)//len(rtn))==(sum(mkn)//len(mkn))):
    print("yes")
else:
    print("no")
