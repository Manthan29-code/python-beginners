#wite a programe to print tirangle
"""for i in range(0,5):
    for j in range(0,5-i):
       print(" ",end='')
    for s in range(0,i+1)
        print("* ",end='')
    print("")"""



#wirte a programe to print square take size of side from user
n=int(input("Enter size of square"))
for i in range(0,n):
    for j in range(0,n):
        if(i==0 or i==n-1 or j==0 or j==n-1 or """i==j or i+j==n-1"""):
            print("♦ ",end="")
        else:
            print("  ",end="")    
    print("")        


