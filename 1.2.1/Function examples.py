# Import turtle
import turtle as trtl

# Make a turtle
james = trtl.Turtle()

def drawSquare(length):
    for sides in range(4):
        james.forward(length)
        james.right(90)

drawSquare(62)
james.forward(100)
drawSquare(67)

wn = trtl.Screen()
wn.mainloop()
