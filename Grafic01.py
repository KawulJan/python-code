from  turtle import*
from random import randint
speed(30)
hideturtle()
def color_1():
    r=randint(0,255)
    b=randint(0,255)
    g=randint(0,255)
    return r,g,b
colormode(255)
bgcolor("black")
for i in range(450):
    forward(i)
    right(89)
    color(color_1())
done()
