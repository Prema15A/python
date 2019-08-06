boh=input()
flagi=0
for i in range(0,len(boh)-1):
  for j in range(i+1,len(boh)):
    if boh[i]<boh[j]:
      flagi=1
      print(boh[j:])
      break
  if flagi==1:
    break
else:
  print(boh)
