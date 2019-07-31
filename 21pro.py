prem=int(input())
maxi=list(map(int,input().split()))
answ=int(prem/2)
run=maxi[:answ]
mon=maxi[answ::]
if ((sum(run)//len(run))==(sum(mon)//len(mon))):
    print("yes")
else:
    print("no")
