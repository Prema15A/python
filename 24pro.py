bwh=int(input())
mph=2**bwh
z=[]
for i in range(0,mph):
    lt=bin(i)[2:].zfill(bwh)
    if(len(lt)<len(bin(2**bwh-1)[2:])):
        z.append([lt.count("1"),lt])
    else:
        z.append([lt.count("1"),lt])
z.sort()
for i in range(len(z)):
    print(z[i][1])
