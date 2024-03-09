#inhertance is process by which one class inherit attribute and method of one or more class
#SINGLE INHARITANCE:-
#       CHILD CLASS HAVE ONLY ONE PARENT CLASS



class Human:
    def __init__(self,num_heart):
        self.num_eyes=2    
        self.num_nose=1    
        self.num_heart=num_heart    
    def Eat(self):
        print("I can eat")
    def Work(self):
        print("I can work")  

class male(Human): # This is single inheritance
# here male is child class of human class(super class)     
    def __init__(self,name,heart):
        super().__init__(heart)   # think, why we need to pass heart as argument       
#super()  is a method it is used to get access of method of parent class
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().Work()
        print("I can code")  
    def Display(self):
        print(f"My name is {self.name} , i have {self.num_heart} Heart")       


man=male("Manthan",1)
print(man.name)
print(man.num_eyes)
man.work()
man.Display()
        