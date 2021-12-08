import pygame
import math
import random
from Simulations import physics as ph
width, height = 1920/2, 1080/2

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("society")


def x_collide(x1, x2, radius):
    if (x2-radius < x1-radius < x2+radius) or (x2-radius < x1+radius < x2+radius):
        return True
    else:
        return False


def y_collide(y1, y2, radius):
    if (y2-radius < y1-radius < y2+radius) or (y2-radius < y1+radius < y2+radius):
        return True
    else:
        return False

p_list = []

for i in range(80):
    p = ph.Particle()
    p.pos = (random.randint(0, width), random.randint(0, height))
    p_list.append(p)

run = True
while run:
    pygame.time.delay(5)
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i, p in enumerate(p_list):

        for i2, p2 in enumerate(p_list):
            if i != i2:

                F = p.Gravitation(p2)

                x1, y1 = p.pos
                x2, y2 = p2.pos

                sin = (y2 - y1)
                cos = (x2 - x1)
                a = max(abs(sin), abs(cos))

                sin = sin / a
                cos = cos / a

                if x_collide(p.pos[0], p2.pos[0], 10) and y_collide(p.pos[1], p2.pos[1], 10):
                    pass

                p.Move(cos * F, sin * F)

                x1, y1 = p.pos
                x2, y2 = p2.pos
                distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

                if distance < 10:
                    a = 15-distance
                    p.Move(cos * -a, sin * -a)

                pygame.draw.circle(win, (0, 255, 0), p.pos, 10)

                """
                x, y = p.pos
                pygame.draw.line(win, (255, 0, 0), (x - 10, y - 10), (x - 10, y + 10))
                pygame.draw.line(win, (255, 0, 0), (x - 10, y - 10), (x + 10, y - 10))
                pygame.draw.line(win, (255, 0, 0), (x + 10, y + 10), (x - 10, y + 10))
                pygame.draw.line(win, (255, 0, 0), (x + 10, y + 10), (x + 10, y - 10))
                """

    pygame.display.update()

pygame.quit()
