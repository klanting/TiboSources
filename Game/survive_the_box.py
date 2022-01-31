import pygame
import random
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Survive The Box")


class Utils():

    @staticmethod
    def wall_generate(amount=10):
        direct = ["left", "right", "up", "down"]

        size = {"left": (60, 20),
                "right": (60, 20),
                "up": (20, 60),
                "down": (20, 60)}
        Walls_cords = []
        for i in range(amount):
            way = random.choice(direct)
            s = size[way]
            data = (random.randint(0, 25)*20, random.randint(0, 25)*20, way, s)
            Walls_cords.append(data)

        return Walls_cords

    @staticmethod
    def coin_generate(width, height, amount=5):
        return [(random.randint(0, 500-width), random.randint(0, 500-height))for i in range(amount)]

    @staticmethod
    def set_text(string, coordx, coordy, fontSize): #Function to set text

        font = pygame.font.Font('freesansbold.ttf', fontSize)
        #(0, 0, 0) is black, to make black text
        text = font.render(string, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (coordx, coordy)
        return (text, textRect)


class Block:
    def __init__(self):
        self.x = 250+1
        self.y = 250+1
        self.width = 50-2
        self.height = 25-2
        self.speed = 5
        self.color = (255, 0, 0)

    def moveUP(self):
        if (self.y - self.speed) >= 0:
            self.y -= self.speed
            return True
        else:
            self.y = 0
            return False

    def moveDOWN(self):
        if (self.y + self.speed) <= (win.get_height()-self.height):
            self.y += self.speed
            return True
        else:
            self.y = win.get_height()-self.height
            return False

    def moveLEFT(self):
        if (self.x - self.speed) >= 0:
            self.x -= self.speed
            return True
        else:
            self.x = 0
            return False

    def moveRIGHT(self):
        if (self.x + self.speed) <= (win.get_width() - self.width):
            self.x += self.speed
            return True
        else:
            self.x = win.get_width() - self.width
            return False

    def getData(self):
        return self.x, self.y, self.width, self.height

    def collide(self, x, y, width, height):
        top_a = self.y
        bottom_a = self.y + self.height
        left_a = self.x
        right_a = self.x + self.width

        top_b = y
        bottom_b = y + height
        left_b = x
        right_b = x + width

        col_width = False
        col_height = False

        if (top_a <= top_b) and (top_b < bottom_a):
            col_height = True
        elif (top_a < bottom_b) and (bottom_b < bottom_a):
            col_height = True

        elif (top_b <= top_a) and (top_a < bottom_b):
            col_height = True
        elif (top_b < bottom_a) and (bottom_a < bottom_b):
            col_height = True

        elif (top_b <= top_a) and (bottom_a < bottom_b):
            col_height = True

        if (left_a <= left_b) and (left_b < right_a):
            col_width = True
        elif (left_a < right_b) and (right_b < right_a):
            col_width = True

        elif (left_b <= left_a) and (left_a < right_b):
            col_width = True
        elif (left_b < right_a) and (right_a < right_b):
            col_width = True

        elif (left_b <= left_a) and (right_a < right_b):
            col_width = True

        if col_width and col_height:
            return True
        else:
            return False

    def collides(self, lst):
        col = False
        for b in lst:
            if self != b:
                if self.collide(b.x, b.y, b.width, b.height) is True:
                    col = True

        return col

    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return ((self.x == other.x) and (self.y == other.y)
                   and (self.width == other.width) and (self.height == other.height))


class Player(Block):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.width = 25
        self.height = 25
        self.speed = 10
        self.color = (0, 0, 255)
        self.lives = 3
        self.score = 0


class Coin(Block):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.color = (0, 255, 255)


class Wall(Block):
    def __init__(self, x, y, way, width, height):
        self.x = x+1
        self.y = y+1
        self.width = width - 2
        self.height = height - 2
        self.speed = 5
        self.color = (255, 0, 0)
        self.way = way

    def move(self):
        if self.way == "left":
            if not super().moveLEFT():
                self.way = "right"
        elif self.way == "right":
            if not super().moveRIGHT():
                self.way = "left"
        elif self.way == "up":
            if not super().moveUP():
                self.way = "down"
        elif self.way == "down":
            if not super().moveDOWN():
                self.way = "up"

    def change_dir(self):
        if self.way == "left":
            self.way = "right"
        elif self.way == "right":
            self.way = "left"
        elif self.way == "up":
            self.way = "down"
        elif self.way == "down":
            self.way = "up"


class Slide(Block):
    def __init__(self, x, y, way, width, height):
        self.x = x + 1
        self.y = y + 1
        self.width = width - 2
        self.height = height - 2
        self.speed = 10
        self.color = (255, 0, 255)
        self.way = way

    def move(self):
        if self.way == "left":
            if not self.moveLEFT():
                self.way = "right"
        elif self.way == "right":
            if not self.moveRIGHT():
                self.way = "left"

    def change_dir(self):
        if self.way == "left":
            self.way = "right"
        elif self.way == "right":
            self.way = "left"

    def moveLEFT(self):
        if (self.x - self.speed) >= 0:
            self.x -= self.speed
            width = True

        else:
            self.x = 0
            width = False

        if (self.y + self.speed) <= (win.get_height()-self.height):
            self.y += self.speed/2
            height = True

        else:
            self.y = win.get_height() - self.height
            height = False

        if (height and width) is True:
            return True
        else:
            return False

    def moveRIGHT(self):
        if (self.x + self.speed) <= (win.get_width() - self.width):
            self.x += self.speed
            width = True

        else:
            self.x = win.get_width() - self.width
            width = False

        if (self.y - self.speed) >= 0:
            self.y -= self.speed/2
            height = True
        else:
            self.y = 0
            height = False

        if (height and width) is True:
            return True
        else:
            return False

run = True
game = True
delay_index = 0
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if game is True:
        """start generate objects"""
        Walls_cords = Utils.wall_generate()

        Walls = []
        Slides = []

        Coins = [Coin(c[0], c[1]) for c in Utils.coin_generate(10, 10, 5)]

        user = Player()
        for w in Walls_cords:
            if not (Wall(w[0], w[1], w[2], w[3][0], w[3][1]).collides(Walls) or user.collide(w[0], w[1], w[3][0], w[3][1])):
                Walls.append(Wall(w[0], w[1], w[2], w[3][0], w[3][1]))
            else:
                solved = False
                while not solved:
                    pot_w = Utils.wall_generate(1)[0]
                    pot_wall = Wall(pot_w[0], pot_w[1], pot_w[2], pot_w[3][0], pot_w[3][1])
                    if not (pot_wall.collides(Walls) or
                            user.collide(pot_w[0], pot_w[1], pot_w[3][0], pot_w[3][1])):
                        Walls.append(pot_wall)
                        solved = True
        """end generate objects"""

    while game:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            user.moveUP()

        if keys[pygame.K_DOWN]:
            user.moveDOWN()

        if keys[pygame.K_LEFT]:
            user.moveLEFT()

        if keys[pygame.K_RIGHT]:
            user.moveRIGHT()

        "visual reset"
        win.fill((0, 0, 0))

        "ticks"

        for a in Walls:
            a.move()

            "check wall collision"
            if a.collides(Walls) is True:
                a.change_dir()

        for s in Slides:
            s.move()

        if (user.collides(Walls) or user.collides(Slides)) is True:
            user.lives -= 1

            spawn_col = True
            while spawn_col:

                x = random.randint(0, win.get_width() - user.width)
                y = random.randint(0, win.get_height() - user.height)

                spawn_col = False
                for a in Walls:
                    if a.collide(x, y, user.width * 2, user.height * 2) is True:
                        spawn_col = True

            user.set_cords(x, y)

            if user.lives == 0:
                game = False

        if user.collides(Coins):
            user.score += 1
            for c in Coins:
                if c.collide(user.x, user.y, user.width, user.height):
                    tup = Utils.coin_generate(10, 10, 1)
                    c.set_cords(tup[0][0], tup[0][1])

            if user.score % 10 == 0:

                spawn_col = True
                while spawn_col:

                    x = random.randint(0, win.get_width() - user.width)
                    y = random.randint(0, win.get_height() - user.height)

                    spawn_col = False
                    if user.collide(x, y, user.width * 2, user.height * 2) is True:
                        spawn_col = True
                Slides.append(Slide(x, y, "left", width=60, height=20))

        "new visuals"
        pygame.draw.rect(win, user.color, user.getData())

        for a in Walls:
            pygame.draw.rect(win, a.color, a.getData())

        for s in Slides:
            pygame.draw.rect(win, s.color, s.getData())

        for c in Coins:
            pygame.draw.rect(win, c.color, c.getData())

        "score visual"
        totalText = Utils.set_text(str(user.score), 30, 25, 50)
        win.blit(totalText[0], totalText[1])

        "live visual"
        totalText = Utils.set_text(str(user.lives), 30, 75, 50)
        win.blit(totalText[0], totalText[1])

        pygame.display.update()

    totalText = Utils.set_text("GAME OVER", 250, 250, 50)
    win.blit(totalText[0], totalText[1])
    totalText = Utils.set_text("press any key to restart", 250, 310, 20)
    win.blit(totalText[0], totalText[1])

    if (delay_index > 50):
        keys = pygame.key.get_pressed()

        if True in keys:
            game = True
            delay_index = 0
    else:
        delay_index += 1

    pygame.display.update()

pygame.quit()

