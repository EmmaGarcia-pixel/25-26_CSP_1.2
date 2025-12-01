import turtle as trtl
james = trtl.Turtle()

james.forward(60)

def drawSquare():
    for sides in range(4):
        james.forward(30)
        james.right(90)

drawSquare()

wn = trtl.Screen()
wn.mainloop()
