gx=int(input())
if gx > 1:
    for dz in range(2,gx):
        if(gx%dz==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')
