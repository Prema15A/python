prem = int(input())
sdx=[]
for i in range(0,prem):
 lun=input()
 sdx.append(lun)
lazzzz=[]
for i in zip(*sdx):
 if(i.count(i[0])==lan(i)):
  lazzzz.append(i[0])
 else:
  break
print(''.join(lazzzz))
