#%%
def quadraticRoots( a, b, c):
    # code here
    ans=[]
    B=-b
    D=((b*2) -(4*a*c) )**(1/2)
    print(D)

    D=int(D)
    ans.append( int((B+D) / (2*a)))
    ans.append( int((B-D) / (2*a)))
    return sorted(ans)
print(quadraticRoots( 1, -2, 1))
# %%
# find no of digit in factorial of n
def digitsInFactorial(N):
        # code here
        ans=1
        for i in range(1,N):
            ans*=i
            print(ans)
        ans*=N    
        print(ans)
        return len(str(ans))    

digitsInFactorial(0)
# %%
# find trialing zero in factorial of n

def trial_zero_M1(N):
    if N<=4:
         return 0
    #s2=0
    s5=0
    for i in range(2,N+1):
        #while(i%2==0):
        #     s2+=1
        #     i=i/2
        while(i%5==0):
             s5+=1
             i=i/5
    #print(s2)               
    print(s5) 
    # return min(s2,s5)  
    # FACT --->s5 is always less then or equal to s2 so there is no need to find min of s2 & s5             
    return s5
    
#print(trial_zero_M1(10))

def trial_zero_M2(N):
     i=5
     ans=0
     while i<=N:
          ans=ans + N/i
          i*=5
     return int(ans)
print(trial_zero_M2(10))
# %%
def isprime(n):
     if n==1:
          return False
     if n==2 or n==3:
          return True
     if n%2==0 or n%3==0:
          return False
     i=5
     while (i*i<n):
          if n%1==0 or n%(i+2)==0:
               return False
          i+=6
     return True     
          
def prime_factor(n):
     if n<1:
          return None
     for i in filter(isprime, range(2,n) ):
          x=i
          while n%x== 0:
               print (x)
               x*=i

prime_factor(128)
 # %%
n=10
for i in range(1,n):  # range is instance object
     print(i)
     n-=2
     print(n)
# %%
# write recusive  solution to find pow(x,n)
#O(log n)     O(logn)
def recursive_power(x,n):
     if n<=0:
          return 1
     if (n%2==0):
          return recursive_power(x,int(n/2))*recursive_power(x,int(n/2))
     else:
         return recursive_power(x,int(n/2))*recursive_power(x,int(n/2))*x    

print(recursive_power(2,8)) 

#iterative solution
def iterative_power(x,n):
     res=1
     while(n>0):
          if n%2!=0:
             res*=x
          n=int(n/2)
          x*=x   
     return res     

print(iterative_power(2,8))
# %%
def doge_count(str):
    count = 0
    for i in range(0,len(str)-3):
         if str[i]=='d' and str[(i+1)]=='o' and str[(i+3)]=='e':
             count = count +1
         
    return count
print(doge_count("dogedopedoze"))

# %%
def isNeighbour(N):
    ##Your code here
    n=N%10
    n1=[8,9,0,1,2]
    if n in n1:
        return True
    else:
        return False
ans_list=filter(isNeighbour,range(3,100))
for i in ans_list:
     print(i,end=" ") 
# %%
str="Manthananma"
s1=str[:int(len(str)/2)]
s=str[len(str):int(len(str)/2)-1:-1]
print(s1)
print(s)

# %%
def removeDuplicates(str):
     nstr=""
     for i in str:
      if i not in nstr:
           nstr+=i
    # for i in s:
    #     print(i)
    #     nstr+=i
     return nstr  
print(removeDuplicates("manthan"))
# %%
def isAnagram(a,b):
        #code here
    check=set(i for i in a)
    for i in check:
        if a.count(i)==b.count(i):
            #print (a.count(i),b.count(i))
            continue
        else:
            return "NO"
    return "YES"
print(isAnagram("allergy","allergic"))
# %%
