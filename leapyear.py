yers=int(input())
if(yers % 4)==0:
    if(yers % 100)==0:
        if(yers % 400)==0:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
else:
    print("no")
        
