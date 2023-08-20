print("enter the numbers for range")
a=int(input())
a2=1
a1=-1
for i in range(0,a):
      s= a1+ a2
      print(s,end=" ")
      a1=a2
      a2=s
      i=i+1
print("\nTHE END")
