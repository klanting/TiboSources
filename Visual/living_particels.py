from vpython import *
import math
import time
"""needs pathfinding"""
floor = box(pos=vector(0, -20, 0), length=40, width=40, height=.1, color=color.white)
ceiling = box(pos=vector(0, 20, 0), length=40, width=40, height=.1, color=color.white)
back = box(pos=vector(0, 0, -20), length=40, width=.1, height=40, color=color.white)
left = box(pos=vector(-20, 0, 0), length=.1, width=40, height=40, color=color.white)
right = box(pos=vector(20, 0, 0), length=.1, width=40, height=40, color=color.white)


class Atom:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.connected = []
        self.visual = sphere(pos=vector(x, 0, z), radius=.75, color=color.orange, opacity=1)
        self.links = {"alpha": {"pos": (1, 0, 0)},
                      "bravo": {"pos": (0, 1, 0)},
                      "charlie": {"pos": (0, 0, 1)},
                      "delta": {"pos": (-1, 0, 0)},
                      "echo": {"pos": (0, -1, 0)},
                      "foxtrot": {"pos": (0, 0, -1)}}

    def check_linked(self, sphere_points):
        """removes not linked atoms"""
        for cur_a in self.connected:
            t_x, t_y, t_z = self.x = cur_a.x, cur_a.y, cur_a.z
            if not ((t_x - self.x) ** 2 + (t_y - self.y) ** 2 + (t_z - self.z) ** 2) ** 1 / 2 < 1.5:
                self.connected.remove(cur_a)

        """adds new linked atoms"""
        for pot_a in sphere_points:
            t_x, t_y, t_z = pot_a.x, pot_a.y, pot_a.z

            """check if it isn't the same point"""
            if not ((t_x == self.x) and (t_y == self.y) and (t_z == self.z)):

                """checks distance to calculate if it is connected or not"""
                if ((t_x-self.x)**2+(t_y-self.y)**2+(t_z-self.z)**2)**1/2 < 1.5:
                    self.connected.append(pot_a)

    def draw_links(self):
        for l in self.links.values():
            x, y, z = l["pos"]
            sphere(pos=vector(self.x+(x/2), self.y+(y/2), self.z+(z/2)), radius=.35, color=color.blue, opacity=1)
atoms = []

for i in range(5):
    x = i*1.5
    for j in range(5):
        z = j*1.5
        atoms.append(Atom(x, 0, z))
print(len(atoms))

for a in atoms:
    a.check_linked(atoms)
    a.draw_links()
print(atoms[0].connected)

