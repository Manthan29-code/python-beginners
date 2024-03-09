def write(n):
    if n==0:
        return
    else:
     # print(f"I am printing hello for {n}") # here i is start from n to 1
      write(n-1)
      print(f"I am printing hello for {n}") # here i is start from 1 to n
n=int(input("how many times do you want to print hello"))
write(n)

#observation 
#if you want to print in descending order simply write statment above the function
# and  for ascending order write statment bellow the function