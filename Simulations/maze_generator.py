import pygame
import random

pygame.init()

win = pygame.display.set_mode((930, 930))

pygame.display.set_caption("maze generator")


class Maze:
    def __init__(self, width, height):
        """setup basic vars"""
        self.maze = []
        self.visited_walls = {(None, None): []}
        self.cell_linked = {}
        self.blocked = []

        for h in range(height):
            width_array = []
            for w in range(width):
                if h % 2 == 0:
                    width_array.append("b")
                elif w % 2 == 0:
                    width_array.append("b")
                else:
                    width_array.append("c")

            self.maze.append(width_array)

        self.generate()

    def generate(self):
        """
        start of the generation process
        First we search for a random cell in the matrix
        """
        while True:
            r_x = random.randint(0, len(self.maze[0]) - 1)
            r_y = random.randint(0, len(self.maze) - 1)

            if self.maze[r_y][r_x] == "c":
                self.cell_linked.update({(r_y, r_x): (None, None)})
                break

        while True:
            pygame.time.delay(50)

            """
            decide the options for the cell to go next, if there is no next available,
            go backwards and check again
            """
            r_y, r_x, lst = self.next_cell(r_y, r_x)

            """
            checks if process is completed
            """
            if r_x is None:
                break

            """chose one of the possible directions"""
            removed = random.choice(lst)

            self.maze[removed[0]][removed[1]] = "r"

            ry, rx = self.find_relative_location((r_y, r_x), removed)

            self.cell_linked.update({(r_y + (2 * ry), r_x + (2 * rx)): (r_y, r_x)})

            r_y += 2 * ry
            r_x += 2 * rx

            self.display()
            pygame.display.update()

        return self.maze, r_x, r_y

    def next_cell(self, r_y, r_x):
        while True:
            """check neighbours of current cell"""
            self.check_neighbours(r_y, r_x)
            lst = self.visited_walls.get((r_y, r_x))

            """If no more available neighbours, start going backwards"""
            if len(lst) == 0:
                t_y, t_x = self.cell_linked.get((r_y, r_x))

                """check if gone backwards to start"""
                if t_y is None:
                    return t_y, t_x, []

                ry, rx = self.find_relative_location((r_y, r_x), (t_y, t_x))

                """prevents to chose the same place again"""
                self.visited_walls[(None, None)].append((r_y + (ry / 2), r_x + (rx / 2)))

                r_y = t_y
                r_x = t_x

            else:
                break

        return r_y, r_x, lst

    def check_neighbours(self, j, i):
        available = []
        """define all neighbour options"""
        neighbours = [(j - 1, i),
                      (j + 1, i),
                      (j, i - 1),
                      (j, i + 1)]

        for n in neighbours:
            found = False

            """check if neighbour isn't already connected to another path"""
            for cell in self.visited_walls.keys():
                if (cell != (j, i)) and (n in self.visited_walls.get(cell)):
                    found = True
                    self.blocked.append(n)

            if (n[0] == 0) or (n[0] == len(self.maze) - 1) or (n[1] == 0) or (n[1] == len(self.maze[0]) - 1):
                found = True

            if n in self.blocked:
                found = True

            if not found:
                available.append(n)

        """update the found walls"""
        self.visited_walls.update({(j, i): available})

        return self.maze

    @staticmethod
    def find_relative_location(cell, neighbour):
        y, x = cell
        j, i = neighbour
        a = j - y
        b = i - x

        return a, b

    def display(self):
        for i, h in enumerate(self.maze):
            for j, w in enumerate(h):

                if w == "b":
                    pygame.draw.rect(win, (0, 100, 50), (j*30, i*30, 30, 30))
                else:
                    pygame.draw.rect(win, (200, 200, 200), (j * 30, i * 30, 30, 30))

    def entrances(self, amount=2):
        options = []

        """random add entrances"""
        for j, h in enumerate(self.maze):
            for i, w in enumerate(h):
                if ((i == 0) or (i == len(self.maze[0])-1)) and (j % 2 != 0):
                    options.append((j, i))
                elif ((j == 0) or (j == len(self.maze)-1)) and (i % 2 != 0):
                    options.append((j, i))

        for i in range(amount):
            y, x = random.choice(options)
            self.maze[y][x] = "c"

    def add_entrance(self, j, i):
        """add specific entrance"""
        self.maze[j][i] = "c"


p = Maze(31, 31)

p.entrances(15)
p.add_entrance(15, 30)
while True:
    p.display()
    pygame.time.delay(50)
    pygame.display.update()
