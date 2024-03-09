#MULTIPLEINHARITANCE:-
# child class will be inharited from more than one class
class Human:
    def __init__(self):
        self.eyes=2
        self.nose=1

    def eat(self):
        print("I can eat")
        
    def walk(self):
        print("I can walk")

    def  work(self):
        print("I can work")    

class Male():
    def __init__(self,name):
        self.name=name

    def  work(self):
        print("I can code") 

class Boy(Human,Male):
    def __init__(self,name):
        Male.__init__(self,name)
        Human.__init__(self) # now you can access atributes of Human class
     
    def work(self):
        print("I can study")

    def run(self):
        print("I can run")

boy_1=Boy("Manthan")
boy_1.work() # here we are accessing work method of boy class
boy_1.eat()

print(Boy.mro())
# mro means METHOD RESOLUTION ORDER
#this method is used to know in which order methodes are invoked
print(boy_1.name)
# print(boy_1.eyes)  it will give error because boy_1 has no attribute eyes
# if we wihs that boy have this attribute the we havt to add Human__init__
# as well as Male.__init__ in boy class 
print(boy_1.eyes)