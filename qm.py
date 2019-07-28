sad=int(input())
iyk=list(map(int,input().split()[:sad]))
iyk.sort()
for i in iyk:
  print(i,end=" ")
