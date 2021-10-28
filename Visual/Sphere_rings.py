from vpython import *
from time import *
import math

floor = box(pos=vector(0, -5, 0), length=10, width=10, height=.1, color=color.white)
ceiling = box(pos=vector(0, 5, 0), length=10, width=10, height=.1, color=color.white)
back = box(pos=vector(0, 0, -5), length=10, width=.1, height=10, color=color.white)
left = box(pos=vector(-5, 0, 0), length=.1, width=10, height=10, color=color.white)
right = box(pos=vector(5, 0, 0), length=.1, width=10, height=10, color=color.white)

core = sphere(radius=.75, color=color.orange, opacity=1)
ring1 = ring(radius=1, length=.1, width=.1, height=.1, color=color.blue, opacity=1)
ring2 = ring(radius=1, length=.1, width=.1, height=.1, color=color.blue, opacity=1)
ring3 = ring(radius=1, length=.1, width=.1, height=.1, color=color.blue, opacity=1)

ring4 = ring(radius=1.1, length=.1, width=.1, height=.1, color=color.red, opacity=1)
ring5 = ring(radius=1.1, length=.1, width=.1, height=.1, color=color.red, opacity=1)
ring6 = ring(radius=1.1, length=.1, width=.1, height=.1, color=color.red, opacity=1)

degree = 0

while True:
    rate(30)
    degree += 5
    rad = math.radians(degree)

    x = math.cos(rad)
    y = math.sin(rad)

    ring1.axis = vector(x, y, 0)
    ring2.axis = vector(0, x, y)
    ring3.axis = vector(y, 0, x)

    ring4.axis = vector(y, x, 0)
    ring5.axis = vector(0, y, x)
    ring6.axis = vector(x, 0, y)

    if degree == 360:
        degree = 0

#curve = curve(pos=lst, length=1, width=1, height=1, opacity=.3)
