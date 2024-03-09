def fir(n):
   
    if (n==0 or n==1):
        return n
    else:
        return fir(n-1) + fir (n-2)
for i in range(10):     
    print(fir(i),end=' ')    
       