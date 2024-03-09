#we can apply for loop on any iterable object of sequential tada typr 
for i in range(1,10):
      print(i,end=" ")

# we can also use else after for as well as while loop
#statment inside else loop will be execute when loop finish

for i in range(6):
     print(i)
     if i==4:      #if we write break statment in else will not execute it means that
         break     # loop was not finished it is breaked    
else: 
      print("sorry no i") 

           