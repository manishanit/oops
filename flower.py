import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    start=1
    end=36
    while(start <= end):
        start1=1
        end1=4
        while(start1<=end1):
            brad.forward(100)
            brad.right(90)
            start1=start1+1
        brad.right(10)
        start=start+1
    window.exitonclick()


draw_shape()
