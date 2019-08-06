boh,sis = map(int,input().split())
costh=0
latd = []
for i in range(boh):
      latd.append(input())
for i in range(boh):
      for j in range(sis-1):
            if latd[i][j] != 'R' and latd[i][j+1] != 'R' :
                  costh+=3
            elif latd[i][j] != 'G' and latd[i][j+1] != 'G':
                  costh+=5
print(costh)
