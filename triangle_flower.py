import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")

    mani = turtle.Turtle()
    mani.color("blue")
    start=1
    end=18
    while(start <= end):
        mani.forward(100)
        mani.left(120)
        mani.forward(100)
        mani.left(120)
        mani.forward(100)
        mani.right(120)
        mani.right(20)
        start=start+1
    mani.right(90)
    mani.forward(200)
    window.exitonclick()


draw_shape()
