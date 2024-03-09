# first program using recursion in life
def fact(a):
    if(a==0 or a==1):
        return 1
    else:
        return a *fact(a-1)
    
a=int(input("Enter a number to find factroial of it"))   
for i in range(10):
      print(fact(i))