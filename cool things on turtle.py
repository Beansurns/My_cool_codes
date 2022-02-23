import turtle
import keyboard
import random
colors = [[37,107,95],[255,255,255]]
t = turtle.Pen()
turtle.colormode(255)
t.speed(0)
turtle.bgcolor(21,21,21)
t.hideturtle()
#.right(-2)
t.pencolor(37, 107, 95)
for i in range(500):
    
    t.width(1)
    t.pencolor(*colors[0])
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    for x in range(2500):
        if keyboard.is_pressed('SPACEBAR'):
            continue
        else:
            
            t.pencolor(*colors[x%2])
            t.width(x//100 + 1)
            #t.forward(2*x)
            #t.left(119)
            #t.forward(2*x)
            #t.left(59)
            t.forward(x+50)
            t.left(89)
        
        
    t.goto(0,0)
    t.clear()
        
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = [r,g,b]
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    abc = [a,b,b]
    
    colors = [rgb,abc]
 