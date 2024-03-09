# make a program to print pascal triangle
#in this program, I have used  the concept of recursion 
def pascal(a,b):
    if(a*b==0 or a==b):
     return 1
    else:
     return pascal(a-1,b-1) + pascal(a-1,b)
    
row=int(input("Enter number for row"))
for i in range(0,row):
    for space in range(0,row - i):
        print("  ",end="")
    for j in range(0,i+1):    
        put=pascal(i,j)
        print(put,"  ",end="")
    print("")    
    
    