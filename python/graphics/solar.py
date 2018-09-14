import turtle, random, math
t = turtle.Turtle(visible=False)
t.speed(0)
turtle.screensize(500,500)
myWin = turtle.Screen()
myWin.bgcolor("black")

def stars(t):
    t.up()
    x = random.randint(-500,500)
    y = random.randint(-500,500)
    t.setpos(x, y)
    t.down()
    t.color("black", "white")
    t.begin_fill()
    t.circle(1)
    t.end_fill()

def orbit():
    def sun(t):
        t.ht()
        t.speed(0)
        t.up()
        t.goto(0,-40)
        t.down()
        t.pencolor('black')
        t.begin_fill()
        t.circle(40)
        t.fillcolor('#ffe297')
        t.end_fill()

    def get_circle(x,y,size,color):
        t=turtle.Turtle()
        t.ht()
        t.speed(0)
        t.up()
        t.goto(x,y)
        t.down()
        t.shape('circle')
        t.shapesize(size,size,None)
        t.color(color)
        t.st()
        t.up()
        return t

    def move(turtle, origin_offset, deg):
        x=origin_offset*math.cos(deg)
        y=origin_offset*math.sin(deg)
        turtle.goto(x,y)

    canvas = turtle.Turtle()
    sun(canvas)
    #(x, y, radius, color)
    orb1 = get_circle(50,0,0.25,'#c09d96')
    orb2 = get_circle(100,0,0.5,'#d58b67')
    orb3 = get_circle(150,0,1,'#5a8a97')
    orb4 = get_circle(200,0,1,'#ff9559')
    orb5 = get_circle(250,0,1.2,'#ffb68d')
    orb6 = get_circle(300,0,1,'#8dd8ff')
    orb7 = get_circle(350,0,0.15,'#74adcb')
    time = 0
    oneS = twoS = threeS = fourS = fiveS = sixS = sevenS = 0
    while time == 0:
        move(orb1, 50, oneS)
        move(orb2, 100, twoS)
        move(orb3, 150, threeS)
        move(orb4, 200, fourS)
        move(orb5, 250, fiveS)
        move(orb6, 300, sixS)
        move(orb7, 350, sevenS)
        oneS=oneS+0.01
        twoS=twoS+0.02
        threeS=threeS+0.03
        fourS=fourS+0.04
        fiveS=fiveS+0.05
        sixS=sixS+0.06
        sevenS=sevenS+0.07


def main():
    count = 0
    if count > 100:
        sount = 0
    while count < 100:
        count = count + 1
        stars(t)
    orbit()
    myWin.exitonclick()

main()
