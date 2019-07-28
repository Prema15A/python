nok,kings=map(int,input().split())
mad=list(map(int,input().split()))
mad.sort()
mad.reverse()
ss=kings
pins=0
for i in mad:
    if(ss>=i):
        ant=int(ss/i)
        pins=pins+ant
        ss=ss-ant*i
    if ss==0:
        break
if(ss==0):
   print(pins)
else:
   print("it's not posiible to select coins in such a way that they sum upto",kings)
