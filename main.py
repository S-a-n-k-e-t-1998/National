import turtle
# import winsound
from playsound import playsound

def Model():
    # creating background screen
    win = turtle.Screen()
    win.setup(width=800,height=600)
    win.bgcolor('black')

    # playing music
    # winsound.PlaySound('atham.mp3',winsound.SND_ASYNC)


    # creating flag
    stand = turtle.Turtle()
    stand.color('white')
    stand.shape('square')
    stand.penup()
    stand.setposition(-100,-280)
    stand.pendown()
    stand.goto(-100,280)

    flag = turtle.Turtle()
    flag.color('white')
    flag.penup()
    flag.setposition(-100,270)
    flag.pendown()

    length = 400
    width = 80

    def rect(color):
        flag.fillcolor(color)
        flag.begin_fill()
        flag.forward(length)
        flag.right(90)
        flag.forward(width)
        flag.right(90)
        flag.forward(length)
        flag.right(180)
        flag.end_fill()

    rect('orange')
    rect('white')
    rect('green')

    flag.left(90)
    flag.forward(width*3)
    flag.hideturtle()

    # drawing wheel
    wheel = turtle.Turtle()
    wheel.color('blue')
    wheel.penup()
    wheel.width(2)
    wheel.goto(100,100)
    wheel.pendown()
    wheel.circle(50)
    wheel.penup()
    wheel.goto(100,150)
    wheel.pendown()
    for i in range(26):
        wheel.forward(48)
        wheel.backward(48)
        wheel.right(13.8)


    # writing text
    text = turtle.Turtle()
    text.hideturtle()
    text.speed(2)

    def write(message,pos,color):
        x,y = pos
        text.color(color)
        text.penup()
        text.goto(x,y)
        text.pendown()
        style = ('Courier',40,'italic')
        text.write(message,font=style)
    def write1(message,pos,color):
        x,y = pos
        text.color(color)
        text.penup()
        text.goto(x,y)
        text.pendown()
        style = ('Courier',20,'italic')
        text.write(message,font=style)    

    write('Happy',(60,-80),'orange')
    write('Independence',(10,-140),'white')
    write('Day 2022',(70,-190),'green')
    write1('Let\'s salute the nation!',(-50,-230),'orange')
    write1('~Sanket Bodake',(-50,-280),'green')
    # making function

    playsound(r"Indian-National-Anthem-\\music.mp3")

    turtle.done()