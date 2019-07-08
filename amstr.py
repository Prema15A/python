ac=int(input())
xwy=ac
sums=0
while ac>0:
  ya=ac%10
  sums=sums+ya*ya*ya
  ac=ac//10
if xwy==sums:
  print("yes")
else:
  print("no")
