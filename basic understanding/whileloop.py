#find the biggest digit from the given number
num=1365
sum=0
x1=0
while num != 0:
    x=num
    x=x % 10
    if(x>=x1):
        x1=x

    print(x,end='') # to print number in reverse order
    sum= sum + x    # to print sum of digite of a given number
    num=int(num /10)
print("\n",sum)
print("the biggest number is",x1)# to print the biggest digit in a given number