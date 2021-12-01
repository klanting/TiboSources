import pygame
import math
from Math import matrices as matrix

width, height = 1920/2, 1080/2

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D-game")


class Cube:
    def __init__(self):
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0

        self.x_rotation = None
        self.y_rotation = None
        self.z_rotation = None

        self.pos = [width//2, height//2]
        self.scale = 600
        self.points = [i for i in range(8)]

        self.points[0] = [[-1], [-1], [1]]
        self.points[1] = [[1], [-1], [1]]
        self.points[2] = [[1], [1], [1]]
        self.points[3] = [[-1], [1], [1]]
        self.points[4] = [[-1], [-1], [-1]]
        self.points[5] = [[1], [-1], [-1]]
        self.points[6] = [[1], [1], [-1]]
        self.points[7] = [[-1], [1], [-1]]

        self.projected_points = []

    def rotate(self, rx, ry, rz):
        self.x_angle += rx
        self.y_angle += ry
        self.z_angle += rz

        self.x_rotation = [[1, 0, 0],
                          [0, math.cos(self.x_angle), -math.sin(self.x_angle)],
                          [0, math.sin(self.x_angle), math.cos(self.x_angle)]]

        self.y_rotation = [[math.cos(self.y_angle), 0, -math.sin(self.y_angle)],
                          [0, 1, 0],
                          [math.sin(self.y_angle), 0, math.cos(self.y_angle)]]

        self.z_rotation = [[math.cos(self.z_angle), -math.sin(self.z_angle), 0],
                          [math.sin(self.z_angle), math.cos(self.z_angle), 0],
                          [0, 0, 1]]

    def edges(self):
        for m in range(4):
            self.connect_point(m, (m + 1) % 4, self.projected_points)
            self.connect_point(m + 4, (m + 1) % 4 + 4, self.projected_points)
            self.connect_point(m, m + 4, self.projected_points)

    @staticmethod
    def connect_point(i, j, k):
        a = k[i]
        b = k[j]
        pygame.draw.line(win, (0, 0, 0), (a[0], a[1]), (b[0], b[1]), 2)

    def D_convert(self):
        index = 0
        self.projected_points = [j for j in range(len(c.points))]

        for point in c.points:
            rotated_2d = matrix.matrix_multiplication(self.x_rotation, point)
            rotated_2d = matrix.matrix_multiplication(self.y_rotation, rotated_2d)
            rotated_2d = matrix.matrix_multiplication(self.z_rotation, rotated_2d)
            distance = 5
            z = 1 / (distance - rotated_2d[2][0])

            projection_matrix = [[z, 0, 0],
                                 [0, z, 0]]

            projected_2d = matrix.matrix_multiplication(projection_matrix, rotated_2d)

            x = int(projected_2d[0][0] * c.scale) + c.pos[0]
            y = int(projected_2d[1][0] * c.scale) + c.pos[1]
            self.projected_points[index] = [x, y]
            pygame.draw.circle(win, (0, 0, 255), (x, y), 10)
            index += 1


c = Cube()

run = True
while run:
    pygame.time.delay(5)
    win.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    c.rotate(0, 0.01, 0)
    c.D_convert()

    # draw edges
    c.edges()

    pygame.display.update()

pygame.quit()