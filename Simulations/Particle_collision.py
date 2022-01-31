import pygame
import random
from Simulations import physics as ph
width, height = 1920/2, 1080/2


pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle collision")


class Particle(ph.Particle):
    def collision(self, x1, x2, y1, y2):
        x, y = self.pos
        Bx = False
        By = False

        if (x1 < x-self.radius < x2) or (x1 < x+self.radius < x2):
            Bx = True

        if (y1 < y-self.radius < y2) or (y1 < y+self.radius < y2):
            By = True

        return Bx, By

    def render(self):
        pygame.draw.circle(win, (0, 255, 0), self.pos, 10)

        x, y = self.pos

        pygame.draw.line(win, (255, 0, 0), (x - 10, y - 10), (x - 10, y + 10))
        pygame.draw.line(win, (255, 0, 0), (x - 10, y - 10), (x + 10, y - 10))
        pygame.draw.line(win, (255, 0, 0), (x + 10, y + 10), (x - 10, y + 10))
        pygame.draw.line(win, (255, 0, 0), (x + 10, y + 10), (x + 10, y - 10))

p_list = []

for i in range(100):
    p = Particle()
    p.pos = (random.randint(0, width), random.randint(0, height))
    p.velocity = (.5, .3)

    p_list.append(p)
run = True
while run:
    pygame.time.delay(5)
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for p in p_list:
        vx, vy = p.velocity
        p.Move(vx, vy)

        """border collision"""
        x, y = p.collision(0, width, 0, height)

        hit_x = False
        hit_y = False
        for h in p_list:
            hx, hy = h.pos
            r = h.radius
            px, py = p.collision(hx-r, hx+r, hy-r, hy+r)

            if (px and py) is True:
                hit_x = True
                hit_y = True

        vx, vy = p.velocity
        if (not x) or (hit_x):
            p.velocity = (vx*-1, vy)
        if (not y) or (hit_y):
            p.velocity = (vx, vy*-1)
        p.render()

    pygame.display.update()

pygame.quit()
