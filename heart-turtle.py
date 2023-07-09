import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("black")
color("#f73487")

begin_fill()

penup()
goto(hearta(0) * 20, heartb(0) * 20)
pendown()

for i in range(10000):
    goto(hearta(i) * 20, heartb(i) * 20)

end_fill()

done()
