def pattern(n):
    if n==0:
      return
    
    pattern(n-1)
    for i in range(n):
        print(i,end="")
    print("")
n=int(input("Enter the length of pattern"))
pattern(n)
  



