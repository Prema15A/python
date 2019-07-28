cut=int(input())
if (cut<=1000):
   for i in range(2,cut):
       if(cut%i==0):
         print("no")
         break
   else:
       print("yes")
else:
    print("no")
