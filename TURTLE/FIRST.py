import turtle as tu

tu.getscreen() # to create screen which is used to draw graphics
t1=tu.Turtle()    # it create turtle(pen) (it can be more then one)
t1.speed(5)
t1.circle(-100,steps=3)
t1.circle(100,steps=3)
 
tu.exitonclick() #to hold screen until we touch on it
