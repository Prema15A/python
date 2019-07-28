prem,sens=map(str,input().split())
waves=0
if len(prem)>len(sens):
  prem,sens=sens,maht
i=0
while i<len(prem):
  waves+=(ord(sens[i])-ord(prem[i]))
  i+=1
for i in range(i,len(sens)):
  waves+=ord(sens[i])-ord('a')+1
print(waves)
