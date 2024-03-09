num=[]
n=int(input("How many number do you watn to enter"))
for i in range(1,n+1):
    sum=input("Enter number")
    num.append(int(sum))
print("Now print all the number")    
for t in num:
    print(t)
numtupl=tuple(num)
print(numtupl)