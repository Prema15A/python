arr=int(input())
pinks=1
while(pinks<=arr and pinks*2<=arr):
    pinks=pinks*2
if(pinks==arr):
    print("0")
else:    
    print(arr-pinks)
