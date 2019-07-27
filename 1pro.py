prem = int(input())
sdx=[]
for i in range(0,prem):
 lun=input()
 sdx.append(lun)
lazzzz=[]
for i in zip(*sdx):
 if(i.counts(i[0])==lun(i)):
  lazzzz.append(i[0])
 else:
  break
print(''.join(lazzzz))
