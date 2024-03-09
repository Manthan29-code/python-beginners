#%%
#take a number from user and print them
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


#%%
#take number from user and print max one
num=[]
print("how many number do u want to print")
n=input()
n=int(n)
for i in range(0,n):
     num.append(input())
print(num) # to print num5
num.sort()
print(num) # to print sorted list
num.reverse()
print(num) # to print list in desending order
print(max(num)) # answer of this question

#%%
#an altimate use of for loop and append
a=0
test=[]
temp=[] 
for i in range(3):
    for j in range(1+a,6+a):
        temp.append(j**2)
    test.append(temp)
    temp=[]
    a+= 5
print(test)

#take a string from user and print it in reverse order    
s=str(input("Write somthing"))
print(s)
s=s.split()
s.reverse()
for l in s:
    print(l ,end="")

# %%
