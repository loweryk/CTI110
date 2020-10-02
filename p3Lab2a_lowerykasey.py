#Using Turtle in Python
#CTI-110 P3LAB2a_LoweryKasey

import turtle          #Allows us to use turtles
wn = turtle.Screen()    #Creates a playground for turtles
alex = turtle.Turtle() #Creatles a turtle, assign to alex

#commands from here to the last line can be replaced

alex.hideturtle() #Hides the turtle in icon

#For the loop that iterates 4 times to draws a square
#Tell alex to draw a square

alex.right(90)        #Tell alex to move right by 90 units
alex.forward(50)      #Tell alex to move forward by 50 units
alex.left(90)         #Tell alex to move left by 90 units                                                  
alex.forward(100)     #Tell alex to move forward by 100 units
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(50)


alex.forward(80)   #Tells alex to draw a specific triangle
alex.left(120) 
alex.forward(80)
alex.left(120)
alex.forward(80)
alex.left(120)

#ends commands
wn.mainloop()   #wait for user to close window
