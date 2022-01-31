import math


class Particle:
    def __init__(self):
        self.mass = 1000000*5
        self.attract_radius = 100
        self.G = 6.674e-11
        self.pos = (0, 0)
        self.radius = 20
        self.velocity = (0, 0)
        self.acceleration = (0, 0)

    def Gravitation(self, p2):
        x1, y1 = self.pos
        x2, y2 = p2.pos
        distance = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
        F = (self.G * (self.mass * p2.mass))/(distance**2)

        if distance <= self.radius:
            return 0
        return F

    def Move(self, x, y):
        x1, y1 = self.pos
        self.pos = x1+x, y1+y


if __name__ == "__main__":
    p = Particle()
    print(p.G)
    p.Move(1, 5)
    print(p.pos)
