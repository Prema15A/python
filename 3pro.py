prem,sor=input().split()
mph=abs(len(prem)-len(sor))
for i in range(len(prem)):
  if len(sor)==1 and sor[i] in prem:
   break
  if prem[i]!=sor[i]:
   mph+=1
print(mph)
