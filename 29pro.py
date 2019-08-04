iyi=int(input())
zas=0
xin=0
boh=[]
while zas<90 and zas<iyi:
  sw=0
  for j in str(iyi-zas):
    sw+=int(j)
  if sw+(iyi-zas)==iyi:
    xin+=1
    boh.append(iyi-zas)
  zas+=1
print(xin)
for zas in boh:
  print(zas)
