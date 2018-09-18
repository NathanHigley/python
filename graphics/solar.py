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
    t.circle(random.randint(1,3))
    t.end_fill()

def orbit():
    def sun(t):
        t.ht()
        t.speed(0)
        t.up()
        t.goto(0,-35)
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
        return t

    def move(t, offset, deg):
        x=offset*math.cos(deg)
        y=offset*math.sin(deg)
        t.goto(x,y)

    sun(turtle.Turtle())
    #lateral distance from center
    x1 = 50
    x2 = 75
    x3 = 100
    x4 = 150
    x5 = 200
    x6 = 250
    x7 = 300
    x8 = 350
    #(x, y, radius, color)
    orb1 = get_circle(x1,0,0.5,'grey')
    orb2 = get_circle(x2,0,0.75,'#d58b67')
    orb3 = get_circle(x3,0,1,'#5a8a97')
    orb4 = get_circle(x4,0,0.9,'#ff9559')
    orb5 = get_circle(x5,0,1.75,'#ffb68d')
    orb6 = get_circle(x6,0,1.5,'#ffe297')
    orb7 = get_circle(x7,0,1.25,'#74adcb')
    orb8 = get_circle(x8,0,1.25,'#74adcb')
    time = 0
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = 0
    while time == 0:
        move(orb1, x1, s1)
        move(orb2, x2, s2)
        move(orb3, x3, s3)
        move(orb4, x4, s4)
        move(orb5, x5, s5)
        move(orb6, x6, s6)
        move(orb7, x7, s7)
        move(orb8, x8, s8)
        #speed variables
        s1=s1+0.08
        s2=s2+0.07
        s3=s3+0.06
        s4=s4+0.05
        s5=s5+0.04
        s6=s6+0.03
        s7=s7+0.02
        s8=s8+0.01

def main():
    c = 0
    while c < 100:
        c = c + 1
        stars(t)
    orbit()
    myWin.exitonclick()

main()
