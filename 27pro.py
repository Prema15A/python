prem,sds=map(int,input().split())
zvz=list(map(int,input().split()))
vmb=list(map(int,input().split()))
tkn=[]
uin=0
for i in range(prem):
    x=vmb[i]/zvz[i]
    tkn.append(x)
while sds>=0 and len(tkn)>0:
    mindex=tkn.index(max(tkn))
    if sds>=zvz[mindex]:
        uin=uin+vmb[mindex]
        sds=sds-zvz[mindex]
    zvz.pop(mindex)
    vmb.pop(mindex)
    tkn.pop(mindex)
print(uin)
