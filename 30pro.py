#vsb
aiy=(input())
cot=0
for i in range(0,len(aiy)):
    skr=(aiy[:i]+aiy[i+1:])
    if(int(skr) % 8==0):
        cot=1
        break
if(cot==1):
    print("yes")
else:
    print("no")
