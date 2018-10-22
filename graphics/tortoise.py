def thing():
    import turtle
    turtle.screensize(600,600)
    turtle.bgcolor("black")
    turt = turtle.Turtle(visible=False)
    turt2 = turtle.Turtle(visible=False)
    turt3 = turtle.Turtle(visible=False)
    turt4 = turtle.Turtle(visible=False)
    turt5 = turtle.Turtle(visible=False)#Second Set
    turt6 = turtle.Turtle(visible=False)
    turt7 = turtle.Turtle(visible=False)
    turt8 = turtle.Turtle(visible=False)
    turt.color("White") # ERASE
    turt2.color("White")
    turt3.color("White")
    turt4.color("White")
    turt2.up()
    turt2.setpos(30,0)
    turt2.down()
    turt4.up()
    turt4.setpos(30,0)
    turt4.down()
    turt.left(140)
    turt2.left(40)
    turt.forward(80)
    turt2.forward(80)
    turt3.left(90)
    turt4.left(90)
    turt3.forward(260)
    turt4.forward(260)
    turt3.left(30)
    turt4.right(30)
    turt3.forward(30)
    turt4.forward(30)
    turt3.right(50)
    turt4.left(50)
    turt3.forward(85)
    turt4.forward(85)
    turt.right(75)
    turt2.left(75)
    turt.forward(80)
    turt2.forward(80)
    turt.left(90)
    turt2.right(90)
    turt.forward(200)
    turt2.forward(200)
    turt.left(170)
    turt2.right(170)
    turt.forward(170)
    turt2.forward(170)
    turt.right(80)
    turt2.left(80)
    turt.forward(150)
    turt2.forward(150)
    turt.left(160)
    turt2.right(160)
    turt.forward(80)
    turt2.forward(80)
    turt.right(90)
    turt2.left(90)
    turt.forward(110)
    turt2.forward(110)
    turt.right(30)
    turt2.left(30)
    turt.forward(52.5)
    turt2.forward(52.5)
    turt5.color("Black") # ERASE
    turt6.color("Black")
    turt7.color("Black")
    turt8.color("Black")
    turt6.up()
    turt6.setpos(30,0)
    turt6.down()
    turt8.up()
    turt8.setpos(30,0)
    turt8.down()
    turt5.left(140)
    turt6.left(40)
    turt5.forward(80)
    turt6.forward(80)
    turt7.left(90)
    turt8.left(90)
    turt7.forward(260)
    turt8.forward(260)
    turt7.left(30)
    turt8.right(30)
    turt7.forward(30)
    turt8.forward(30)
    turt7.right(50)
    turt8.left(50)
    turt7.forward(85)
    turt8.forward(85)
    turt5.right(75)
    turt6.left(75)
    turt5.forward(80)
    turt6.forward(80)
    turt5.left(90)
    turt6.right(90)
    turt5.forward(200)
    turt6.forward(200)
    turt5.left(170)
    turt6.right(170)
    turt5.forward(170)
    turt6.forward(170)
    turt5.right(80)
    turt6.left(80)
    turt5.forward(150)
    turt6.forward(150)
    turt5.left(160)
    turt6.right(160)
    turt5.forward(80)
    turt6.forward(80)
    turt5.right(90)
    turt6.left(90)
    turt5.forward(110)
    turt6.forward(110)
    turt5.right(30)
    turt6.left(30)
    turt5.forward(52.5)
    turt6.forward(52.5)

def solar():
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
        t.circle(random.randint(1,2))
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
        thing()
        orbit()
        myWin.exitonclick()

    main()



import tkinter as tk
root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("BEHOLD")
root.minsize(525, 250)
root.maxsize(525, 250)
a = tk.Button(root, text="SOLAR",font=('courier', '20') ,command=solar)
b = tk.Button(root, text="GEASS",font=('courier', '20') ,command=thing)
t1 = tk.Label(root, text="\nSOLAR is Nathan's take on displaying an animated solar system,\nfeaturing Evan's ""constellation."" Utilizing randomized star\nlocations,and eight concurrent turtles circling the center\nat varying distances and speeds, a unique animation unfolds.",font=('courier', '10'))
t2 = tk.Label(root, text="\nGEASS is Evan's meticulous drawing of a Geass emblem\nfrom his third-and-a-half favorite anime.\nYeah.",font=('courier', '10'))
a.pack()
b.pack()
t1.pack()
t2.pack()
root.mainloop()
