mn=[]
rs=[]
for i in range(2):
	xe1,yh1=map(int,input().split())
	mn.append(xe1)
	rs.append(yh1)
print(abs(mn[0]-mn[1]),abs(rs[0]-rs[1]),sepd=' ')
