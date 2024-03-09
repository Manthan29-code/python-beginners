class Human:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    def Showdata(self):
         print(f"Heyy,My name is {self.name} and i am {self.age}.")
    def Eat(self):    
          print("I can eat")

class Male(Human):
     def work(self):
         print("I am businessmen.")

class Female(Human):
     def work(self):
         print("I am housewife")

male_1=Male("Manthan",18)
female_1=Female("Kavita",16)  
print(male_1.age)
female_1.work()       
female_1.Showdata()       
female_1.Eat()       