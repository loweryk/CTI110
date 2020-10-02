#Program uses the turtle in python
#CTI-110 P3LAB2b_lowerykasey

import turtle
wn = turtle. Screen()
kasey = turtle.Turtle()

#tell turtle to write letter K 

kasey.pensize(5)
kasey.pencolor('green')


kasey.penup()
kasey.hideturtle()
kasey.goto(-50,0)
kasey.write('K', font=('High Tower Text', 42))
kasey.pendown()

#tell turtle to write letter L

kasey.penup()
kasey.hideturtle()
kasey.goto(50,0)
kasey.write('L', font=('High Tower text', 42))
kasey.pendown()

wn.mainloop()


