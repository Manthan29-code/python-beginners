row=5
for i in range(0,row+1):
    for space in range(0,row-i+1):
        print(" ",end="")
    for j in range(0,i+1):
      if (j*i==0 ):
         coef=1
         
      else:
         coef*=(i-j+1)/j  # I don't know what is logic behind this statment
      print(int(coef)," ",end="")
    print("")  