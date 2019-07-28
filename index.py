prem=int(input())
swd=list(map(int,input().split()[:prem]))
for sq in range(prem):
  print(swd[sq],sq)
