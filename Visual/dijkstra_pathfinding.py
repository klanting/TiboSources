import pygame
import math
import random
from Tools import authentication as au
width, height = 1920/2, 1080/2

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("pathfinding")


class Map:
    def __init__(self):
        self.roads = []
        self.junctions = set()
        self.jun_dict = {}
        self.jun_pos = {}

    def junction_add(self, pos):
        auth, authset = au.generate(self.junctions, 5)

        self.junctions.add(auth)

        self.jun_pos.update({auth: pos})
        self.jun_dict.update({auth: set()})

    def junction_dis(self, j1, j2):
        x1, y1 = self.jun_pos[j1]
        x2, y2 = self.jun_pos[j2]

        dis = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
        return dis

    def road_add(self, j1, j2, cost):
        self.roads.append((j1, j2, cost))

        self.jun_dict[j1].add(j2)
        self.jun_dict[j2].add(j1)

    def has_road(self, j1, j2):
        if j2 in self.jun_dict[j1]:
            return True
        else:
            return False

    def get_road(self, j1, j2):
        for r in self.roads:
            fj1, fj2, cost = r
            normal = (j1 == fj1) and (j2 == fj2)
            invers = (j1 == fj2) and (j2 == fj1)
            if normal or invers:
                return r
        return None

    def render(self):
        for j in self.jun_pos.values():
            pygame.draw.circle(win, (0, 0, 255), j, 10)
        for r in self.roads:
            j1, j2, cost = r

            pygame.draw.line(win, (0, 0, 0), self.jun_pos[j1], self.jun_pos[j2], 2)

    def find_path(self, start, end):
        open = {start}
        open_cost = {start: 0}
        closed = set()
        linking = {}

        while True:
            """if path don't exists"""
            if len(open) == 0:
                return None

            """search for best"""
            best = None
            best_cost = math.inf
            for key in open_cost.keys():
                value = open_cost.get(key)

                if value < best_cost:
                    best = key
                    best_cost = value

            """checks when arrived"""
            if best is end:
                backwards = best
                path = [best]

                searching = True
                while searching:
                    if backwards in linking.keys():
                        path.append(linking[backwards])
                        backwards = linking[backwards]
                    else:
                        searching = False

                return path

            """finds all the neigbours"""
            for n in sorted(self.jun_dict[best]):
                if not ((n in closed) or (n in open)):
                    j1, j2, cost = self.get_road(best, n)

                    open.add(n)
                    open_cost.update({n: cost+open_cost[best]})
                    linking.update({n: best})

            open.remove(best)
            open_cost.pop(best)
            closed.add(best)

map = Map()

for i in range(15):
    x = random.randint(0, width)
    y = random.randint(0, height)
    map.junction_add((x, y))


for i in range(25):
    a = random.sample(map.junctions, 1)[0]
    b = random.sample(map.junctions, 1)[0]

    if a is not b:
        if not map.has_road(a, b):
            v = map.junction_dis(a, b)
            map.road_add(a, b, v)

"""map.junction_add((50, 80))

map.junction_add((300, 50))

map.junction_add((90, 100))

map.road_add(sorted(map.junctions)[0], sorted(map.junctions)[2], random.randint(1, 100))
map.road_add(sorted(map.junctions)[1], sorted(map.junctions)[2], random.randint(1, 100))
"""

c = random.choice(sorted(map.junctions))
d = c
while d == c:
    d = random.choice(sorted(map.junctions))
if map.has_road(c, d):
    print(map.get_road(c, d))
map.render()
print(c, d)
print(map.find_path(c, d))


run = True
while run:
    pygame.time.delay(5)
    win.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    map.render()

    """mark the path"""
    pygame.draw.circle(win, (255, 0, 0), map.jun_pos[c], 10)
    pygame.draw.circle(win, (255, 0, 0), map.jun_pos[d], 10)

    if not map.find_path(c, d) is None:
        lst = map.find_path(c, d)
        for i, e in enumerate(lst):
            if len(lst) > i + 1:
                r = map.get_road(e, lst[i + 1])

                j1, j2, cost = r

                pygame.draw.line(win, (0, 255, 0), map.jun_pos[j1], map.jun_pos[j2], 2)

    pygame.display.update()

pygame.quit()
