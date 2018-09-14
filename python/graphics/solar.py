import turtle, random, math
t = turtle.Turtle(visible=False)
t.speed(0)
turtle.screensize(800,800)
myWin = turtle.Screen()
myWin.bgcolor("black")

def stars(t):
    t.up()
    x = random.randint(-800,800)
    y = random.randint(-800,800)
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
        t.circle(35)
        t.fillcolor('yellow')
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

    def move(t, offset, deg):
        x=offset*math.cos(deg)
        y=offset*math.sin(deg)
        t.goto(x,y)

    sun(turtle.Turtle())
    #(x, y, radius, color)
    orb1 = get_circle(50,0,0.5,'grey')
    orb2 = get_circle(75,0,0.75,'#d58b67')
    orb3 = get_circle(100,0,1,'#5a8a97')
    orb4 = get_circle(150,0,0.9,'#ff9559')
    orb5 = get_circle(200,0,1.75,'#ffb68d')
    orb6 = get_circle(250,0,1.5,'#ffe297')
    orb7 = get_circle(300,0,1.25,'#74adcb')
    orb8 = get_circle(350,0,1.25,'#74adcb')
    time = 0
    oneS = twoS = threeS = fourS = fiveS = sixS = sevenS = eightS = 0
    while time == 0:
        move(orb1, 50, oneS)
        move(orb2, 75, twoS)
        move(orb3, 100, threeS)
        move(orb4, 150, fourS)
        move(orb5, 200, fiveS)
        move(orb6, 250, sixS)
        move(orb7, 300, sevenS)
        move(orb8, 350, eightS)
        oneS=oneS+0.08
        twoS=twoS+0.07
        threeS=threeS+0.06
        fourS=fourS+0.05
        fiveS=fiveS+0.04
        sixS=sixS+0.03
        sevenS=sevenS+0.02
        eightS=eightS+0.01

def main():
    c = 0
    while c < 100:
        c = c + 1
        stars(t)
    orbit()
    myWin.exitonclick()

main()
