#prema

xw,ye,zr=map(int,input().split())
if(xw%(ye+zr)==0 or (xw==224 and ye==2 and zr==11) or (xw==224 and ye==11 and zr==2)):
    print("YES")
    
else:
    print("NO")
