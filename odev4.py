sayac = 0;
for x in range(99,1000):
       a =str(x)
       if(a[0] != a[1] and a[1] != a[2] and a[0] != a[2]):
               sayac = sayac +1
               print(a)
       else:
               sayac = sayac

print(sayac)