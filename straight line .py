import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to the starting position
t.penup()  # Lift the pen to move without drawing
t.goto(-100, 0)  # Set the starting position
t.pendown()  # Lower the pen to start drawing

# Draw a straight line
t.forward(200)  # Move forward 200 units

# Keep the window open until it's closed by the user
turtle.done()
