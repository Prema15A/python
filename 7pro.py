are=int(input())
pinks=1
while(pinks<=are and pinks*2<=any):
    pinks=pinks*2
if(pinks==are):
    print("0")
else:    
    print(are-pinks)
