#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "lavender"
score = 0

#-----initialize turtle-----
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()

#------game functions-------
def spot_clicked(x,y):
    print("Meowl was clicked")
    newX = rand.randint(-300,300)
    newY = rand.randint(-300,300)
    meowl.goto(newX,newY)
    update_score()

def change_position():
    # Move the turtle to a random location
    newX = rand.randint(-300,300)
    newY = rand.randint(-300,300)
    meowl.goto(newX, newY)

def update_score():
    # include the global score
    global score
    # Increment the score by 1
    score += 1
    # print the score
    print(score)

#----------events-----------
meowl.onclick(spot_clicked)


wn = trtl.Screen()
wn.mainloop()