mz=input()
re=mz.lstrip('-').replace('.','',1).isdigit()
if(re==True):
	print("yes")
else:
	print("No")
