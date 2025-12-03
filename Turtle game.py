#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "lavender"

#-----initialize turtle-----
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)

#------game functions-------
def spot_clicked(x,y):
    print("Meowl was clicked")
    newX = rand.randint(-300,300)
    newY = rand.randint(-300,300)
    meowl.goto(newX,newY)

#----------events-----------
meowl.onclick(spot_clicked)


wn = trtl.Screen()
wn.mainloop()