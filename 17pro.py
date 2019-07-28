prem,sun = input().split()
sun = int(sun)
fakes = False
bin = list(map(int,input().split()))
for i in range(len(bin)):
    for j in range(len(bin)):
        if bin[i]+bin[j] == sun:
            fakes = True
print("yes" if fakes else "no") 
