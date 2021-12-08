import pygame
import random
from Simulations import child as ch
from Tools import authentication as au
import matplotlib.pyplot as pyplot
from matplotlib import style
width, height = 1920/2, 1080/2

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("society")

auth_list = set()


class Life:
    def __init__(self):
        global auth_list
        self.auth, auth_list = au.generate(auth_list)
        self.gen_list = ch.Birth.generate(5, base_gen1, base_gen2)
        self.age = 0
        self.pos = (random.randint(0, width), random.randint(0, height))
        self.fertile = False
        self.available = True
        self.dead = False
        self.partner = None
        self.kids = 0

        if ch.Genome.is_dominant(self.gen_list[0], "Y"):
            self.male = True
        else:
            self.male = False

    def is_fertile(self):
        return self.fertile

    def is_available(self):
        return self.available

    def aging(self):
        global fertile_cop
        self.age += 1

        if self.age > 18:
            self.fertile = True
            self.find_partner(living)

        if (self.partner is not None) and (self.available is True) and (self.partner.available is True):
            fertile_cop += 1

            value = random.random()

            if value > 0.75:
                living.append(Life())
                self.kids += 1
                self.partner.kids += 1

                stop = random.random()

                if stop > 0.52:
                    self.available = False
                    self.partner.available = False

        if self.age > 40:
            self.available = False
            self.fertile = False

        if self.age > 50:
            value = random.random()
            if (value*100) > 150-self.age:
                self.dead = True

    def is_dead(self):
        return self.dead

    def render(self):
        if self.male:
            color = (0, 0, 255)
        else:
            color = (255, 0, 255)

        pygame.draw.circle(win, color, self.pos, 2)

    def find_partner(self, livings):
        if self.partner is None:
            for lf in reversed(livings):
                if (lf is not self) and (lf.partner is None):
                    if lf.male is not self.male:

                        if lf.available is self.available:
                            self.partner = lf
                            lf.partner = self

                            self.set_pos(lf.pos)
                            break

    def set_pos(self, pos):
        x, y = pos
        self.pos = (x, y+3)


base_gen1 = [("X", "Y"),
             ("B", "B"),
             ("C", "C"),
             ("D", "D"),
             ("E", "E")]

base_gen2 = [("X", "X"),
             ("B", "B"),
             ("C", "C"),
             ("D", "D"),
             ("E", "E")]

living = [Life() for i in range(100)]
index = 0

index_lst = [i for i in range(1000)]
score_lst = []
m_lst = []
w_lst = []
a_lst = []
fertile_copples = []

kids = 0
parents = 0

run = True
while run:
    pygame.time.delay(5)
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    a = 0
    fertile_cop = 0
    for life in living:

        life.aging()

        if life.dead:
            living.remove(life)
            if life.partner is not None:
                life.partner.partner = None

            parents += 1
            kids += life.kids

        life.render()

        if life.available:
            a += 1

    a_lst.append(a)
    fertile_copples.append(fertile_cop*2)


    print(len(living), a)
    score_lst.append(len(living))

    males = 0
    females = 0
    for l in living:
        if l.male:
            males += 1
        else:
            females += 1

    m_lst.append(males)
    w_lst.append(females)

    index += 1

    if index == 1000:
        run = False

    pygame.display.update()

pygame.quit()

style.use("ggplot")
print(len(index_lst))
print(len(score_lst))
print(kids/parents)

pyplot.plot(index_lst, score_lst)
pyplot.plot(index_lst, m_lst)
pyplot.plot(index_lst, w_lst)
pyplot.plot(index_lst, a_lst)
pyplot.plot(index_lst, fertile_copples)
pyplot.xlabel("time")
pyplot.ylabel("value")
pyplot.show()
