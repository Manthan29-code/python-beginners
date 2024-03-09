# concept of class method
# you will learn how to create class method and use it
class instructor:
    follower=0 #class object variable
    def __init__(self,name,address): # here self means object created by us
        print("New oject created ")
        self.name=name
        self.address=address

    def display(self,college):
        print(f"Hi, I am {self.name}.")
        print ("I am from",self.address)
        print ("I am study in ",college)

    def updatefollower(self,):  # this method will increases your followr by 1
        print(f"Now your follower are {self.follower +1}")   
        
            
obj_1=instructor("manthan","ahmedabad") #obj_1 created 
# print(obj_1.name)
# print(obj_1.address)
# Now we can use display method to print name and address
obj_1.display("L.D.")
obj_1.updatefollower()
