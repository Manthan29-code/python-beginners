# there are two types of argument
#1)positional & 2) keyword argument 


def info(name, place,):
    print(f"Hi, My name is {name}")
    print(f"I am from {place}")

info("manthan","Ahmedabad")   
info("Ahmedabad","manthan") # both are positional argument  
info(name="manthan",place="Ahmedabad")
info(place="Ahmedabad",name="manthan") # both are keyword argument  
#info(name="manthan","Ahmedabad") 
# #It will give error becouse
#positional argument follws keyword argument

#info("Ahmedabad",name="manthan") 
# this also note right way 
#becouse we have already declared Ahmedabad as value of name 
# so now we con assigne another value to the name
info("Ahmedabad",place="manthan")

print("***************************************************************************************")

def sum(*number):   # *number will take all the positional arguments as tuple
   print(number)
   c=0
   for i in number:
       c=c+i
   print(f"sum of the numbers is {c}")
       
   
sum(3,5,2,7)   
sum(3,8,4,2,4)   