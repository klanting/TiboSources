from vpython import *
import math
import random

floor = box(pos=vector(0, -5, 0), length=10, width=10, height=.1, color=color.white)
ceiling = box(pos=vector(0, 5, 0), length=10, width=10, height=.1, color=color.white)
back = box(pos=vector(0, 0, -5), length=10, width=.1, height=10, color=color.white)
left = box(pos=vector(-5, 0, 0), length=.1, width=10, height=10, color=color.white)
right = box(pos=vector(5, 0, 0), length=.1, width=10, height=10, color=color.white)

core = sphere(radius=.75, color=color.orange, opacity=1)


def fibonacci_sphere(samples, dif):
    pts = []
    phi = math.pi * (3. - math.sqrt(5.))

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2
        radius = math.sqrt(1 - y * y)
        radius += (dif[i])

        theta = phi * i

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        y = y * (1 + dif[i])

        pts.append((x, y, z))

    return pts


sphere_list = []

difference = [random.random() for i in range(1000)]

for point in fibonacci_sphere(len(difference), difference):
    sphere_list.append(sphere(pos=vector(point[0], point[1], point[2]), radius=.1, color=color.blue))
