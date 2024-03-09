class Line:
    def __init__(self, coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    def distance(self): 
        return ((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)**(0.5)
    def slope(self):
        if((self.coor2[0]-self.coor1[0])==0):
            print ("it is vartical line")
        else:       
           print((self.coor2[1]-self.coor1[1]) / (self.coor2[0]-self.coor1[0]))
    


question1=Line((3,4),(3,6))
dis=question1.distance()
print("Distance between two pont is ",dis)
print(question1.distance())
question1.slope()


print("*******************************************************************************")
class Cylinder:
    def __init__(self,height=1,radius=1):
        self.h=height        
        self.r=radius
    def volume(self):
        print(2*3.14*self.r*self.r*self.h)
    def surface_area(self):
        print(2*3.14*(self.r)*(self.r + self.h))


c=Cylinder(2,3)
c.volume()
c.surface_area()