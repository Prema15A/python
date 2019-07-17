mwn = int(input())
nqn = list(map(int,input().split()[:mwn]))
yay = sorted(nqn)
for i in yay:
    print(i,end=" ")
