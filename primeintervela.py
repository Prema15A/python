dv,yw=map(int,input().split())
for uq in range(dv+1,yw):
    for vo in range(2,uq):
       if(uq%vo==0):
           break
    else:   
        print(uq,end=" ")
