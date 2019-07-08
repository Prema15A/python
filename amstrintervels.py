ku,ny=map(int,input().split())
for mr in range(ku+1,ny):
    sums=0
    nums=mr
    while nums>0:
        dig=nums%10
        sums+=digs**3
        nums//=10
        if(mr==sums):
            print(mr,end=" ")
