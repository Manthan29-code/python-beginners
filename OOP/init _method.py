#init method in python is equivelent to constructor in c++
# it used to initializes object in python

class instructor:
    def __init__(self,name,address): # here self means object created by us
        print("New oject created ")
        self.name=name
        self.address=address

obj_1=instructor("manthan","ahmedabad") #obj_1 created 
#obj_1.name="manthan"       #here we are creating attribute for class instructor
#print("My name is",obj_1.name)
print(obj_1.name)
print(obj_1.address) 