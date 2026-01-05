#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.penup()
drawer = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

# This function takes care of font and color.
def draw_an_A():
  drawer.color("white")
  drawer.write("A", font=("Arial", 14, "bold"))
  apple.goto(0, -500)

wn.onkeypress(draw_an_A, "a")

#-----function calls-----
draw_apple(apple)
wn.listen()
wn.mainloop()