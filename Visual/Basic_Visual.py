from vpython import *
from time import *
import math
floor = box(pos=vector(0, -5, 0), length=10, width=10, height=.1, color=color.white)
ceiling = box(pos=vector(0, 5, 0), length=10, width=10, height=.1, color=color.white)
back = box(pos=vector(0, 0, -5), length=10, width=.1, height=10, color=color.white)
left = box(pos=vector(-5, 0, 0), length=.1, width=10, height=10, color=color.white)
right = box(pos=vector(5, 0, 0), length=.1, width=10, height=10, color=color.white)

core = sphere(radius=.75, color=color.blue)
atom1 = sphere(pos=vector(0, 0, 0), radius=.75, color=color.green)
atom2 = sphere(pos=vector(0, 0, 0), radius=.75, color=color.green)
atom3 = sphere(pos=vector(0, 0, 0), radius=.75, color=color.green)

atom4 = sphere(pos=vector(0, 0, 0), radius=.75, color=color.red)
atom5 = sphere(pos=vector(0, 0, 0), radius=.75, color=color.red)
atom6 = sphere(pos=vector(0, 0, 0), radius=.75, color=color.red)

degree = 0
while True:
    rate(20)
    degree += 10
    rad = math.radians(degree)
    c = 4 * math.cos(rad)
    s = 4 * math.sin(rad)

    atom1.pos = vector(0, s, c)
    atom2.pos = vector(c, 0, s)
    atom3.pos = vector(s, c, 0)

    rad = math.radians(degree+180)
    c = 4 * math.cos(rad)
    s = 4 * math.sin(rad)

    atom4.pos = vector(0, s, c)
    atom5.pos = vector(c, 0, s)
    atom6.pos = vector(s, c, 0)