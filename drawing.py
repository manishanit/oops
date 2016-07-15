import turtle

def draw_shape():
    window =turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    start=1
    end=4
    while(start <= end):
        brad.forward(100)
        brad.right(90)
        start=start+1

    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


    mani=turtle.Turtle()
    mani.color("yellow")
    mani.forward(100)
    mani.left(120)
    mani.forward(100)
    mani.left(120)
    mani.forward(100)
    mani.right(120)
    
    window.exitonclick()

draw_shape()
