def digit(n):
    if n<=0:
        return
    a=n%10
    b=n/10
    digit(int(b)) 
    print(int(a))
    
   
n=int(input("Enter a number to print digit in it "))
#print(digit(n))
digit(n)