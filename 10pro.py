aut=int(input())
bon=[int(i) for i in input().split()]
xon=0
for k in range(aut):
   for j in range(k):
      if bon[j]<bon[k]:
         xon+=bon[j]
print(xon) 
