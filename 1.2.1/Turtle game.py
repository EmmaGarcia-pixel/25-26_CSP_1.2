#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "lavender"
score = 0
font_setup = ("Arial", 20, "normal")

#-----initialize turtle-----
# Turtle to draw the score
score_writer = trtl.Turtle()
score_writer.penup()

# Turtle to draw a box
box_turtle = trtl.Turtle()
box_turtle.penup()

# Shape turtle
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()

# Timer
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# Turtle to write the countdown
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()

#------game functions-------
# Set starting location
counter.goto(-400, 325)

# Write the timer
def countdown():
  global timer, timer_up
  counter.clear()
  # if counter finishes write "Times Up."
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True

'''
    
      if score > 20:
        score_writer.write("You win!")
      else:
        score_writer.write("You lose!")
        
'''

  # If not then write Timer: (the amount of time left)
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

# Draw the box for the score
def scoreBox():
    # Set up the starting location and pendown
    box_turtle.goto(275, 325)
    box_turtle.pendown()

  # Draw the box
    for sides in range(2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(50)
        box_turtle.left(90)

    #Place score_writer where it will write the score
    score_writer.penup()
    score_writer.goto(300, 332)

    score_writer.hideturtle()
    box_turtle.hideturtle()

# Get a score boost, move the turtle randomly
def spot_clicked(x,y):
    change_position()

def change_position():
    # Move the turtle to a random location
    newX = rand.randint(-300,300)
    newY = rand.randint(-300,300)
    meowl.goto(newX, newY)
    update_score()

def update_score():
    # include the global score
    global score
    # Increment the score by 1
    score += 1
    # Clear out the prior score
    score_writer.clear()
    # print the current score
    score_writer.write(score, font=font_setup)

#----------events-----------
meowl.onclick(spot_clicked)

scoreBox()
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()