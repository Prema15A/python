utc=int(input())
if utc!=0:
	print(1,end=' ')
	op=1
	kic=0
	for i in range(1,utc):
		zsc=kic+op
		print(zsc,end=' ')
		kic=op
		op=zsc
else:
	print(0)
