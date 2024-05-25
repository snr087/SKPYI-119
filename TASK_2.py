from turtle import *
flag = Turtle()
wd = title("indian flag")
flag.speed(0)
flag.right(90)
flag.fd(300)
flag.backward(500)
flag.home()
def rec(distance,color):#creating function for rectangular blocks 
    flag.goto(0,distance)
    flag.begin_fill()
    for i in range(2): 
        flag.fd(300)
        flag.rt(90)
        flag.fd(80)
        flag.rt(90)
    flag.fillcolor(color)
    flag.end_fill()
rec(200,"orange")#calling every function wuith color  
rec(120,"white")
rec(40,"green")
flag.up()#drawing center circle
flag.goto(150,59)
flag.down()
def fun():
    flag.penup()
    flag.goto(150,83)
    flag.pendown()
flag.color("blue")
flag.circle(25)
k=0
for i in range(24):
    fun()
    k += 15
    flag.left(k)
    flag.fd(25)
flag.hideturtle()
exitonclick()
#program complete
