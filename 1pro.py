xp = int(input())
	strng1 = []
	for yr in range(0,xp):
	    strng = input()
	    strng1.append(strng)
	

	yr = 0
	zq = 0
	flag = True
	for b in range(0,len(strng1[0])):
	    if(flag==False):
	        break
	    sw=1
	    while(sw<xp and strng1[0][yr]==strng1[sw][yr]):
	        sw+=1
	    if(sw==xp):
	        zq+=1
	    else:
	        flag = False
	        break
	    
	for yr in range(0,zq):
	    print(strng1[0][yr],end="")


