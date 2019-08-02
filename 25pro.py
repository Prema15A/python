nak=int(input())
lap=input().split()
sfs=[]
for i in range(nak):
    sgr=lap[i]
    for j in range(i+1,nak):
        if(int(lap[i])<int(lap[j]))and (int(lap[j-1])<int(lap[j])):
            sgr+=lap[j]
        else:
            break
    sfs.append(len(sgr))
print(max(sfs))
