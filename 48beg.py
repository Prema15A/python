nom=int(input())
vetr=list(map(int,input().split()[:nom]))
print(sum(vetr)//nom)
