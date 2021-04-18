import pygame
import sys
import math
import random

'''
Made by F.S.
Distributed 2/25/20
'''

pygame.init()

width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Motion")
clock = pygame.time.Clock()


white = (255, 255, 255)
black = (0, 0, 0)
blue = (52, 174, 235)
red = (240, 55, 58)
yellow = (249, 247, 86)
orange = (248, 176, 42)
center = (width//2, height//2)

y = 0
x = 0
width_rect = 700
height_rect = 700
w = width_rect/2
h = height_rect/2
rect = ((center[0]-(width_rect/2), center[1]-(height_rect/2)), (width_rect, height_rect))
x_left = 200
x_right = 600
corner_sensitivity = 50

corners = [[[center[0]-w, center[0]-w+corner_sensitivity], [center[1]-h, center[1]-h+corner_sensitivity]],
           [[center[0]-w, center[0]-w+corner_sensitivity], [center[1]+h, center[1]+h-corner_sensitivity]],
           [[center[0]+w, center[0]+w-corner_sensitivity], [center[1]-h, center[1]-h+corner_sensitivity]],
           [[center[0]+w, center[0]+w-corner_sensitivity], [center[1]+h, center[1]+h-corner_sensitivity]]]

corner_points = [[center[0]-w, center[1]-h], [center[0]-w, center[1]+h], [center[0]+w, center[1]-h], [center[0]+w, center[1]+h]]
print(corner_points)
corner_points_x_offsets = [
                            [corner_points[0][0]+corner_sensitivity, corner_points[0][1]],
                            [corner_points[1][0]+corner_sensitivity, corner_points[1][1]],
                            [corner_points[2][0]-corner_sensitivity, corner_points[2][1]],
                            [corner_points[3][0]-corner_sensitivity, corner_points[3][1]]
                            ]

corner_points_y_offsets = [
                            [corner_points[0][0], corner_points[0][1]+corner_sensitivity],
                            [corner_points[1][0], corner_points[1][1]-corner_sensitivity],
                            [corner_points[2][0], corner_points[2][1]+corner_sensitivity],
                            [corner_points[3][0], corner_points[3][1]-corner_sensitivity]
                            ]

corner_values = [white, white, white, white]

x_direction = 1
y_direction = 1
circle_radius = 15

x_speed = 2
y_speed = 2
x_i = 0
y_i = 0

class Ball:
    def __init__(self, color, radius, x_speed = 2, y_speed = 2, random_factor = 3, x_direction = 1, y_direction = 1):
        self.color = color
        self.radius = radius
        self.start = [random.randint(center[0]-(w//2), center[0]+(w//2)), random.randint(center[1]-(h//2), center[1]+(h//2))]
        self.random_factor = random_factor
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_i = 0
        self.y_i = 0
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.x = 0
        self.y = 0
        self.circle = ()
        self.n_i = 0

    def cycle(self):
        self.circle = (self.start[0] + self.x, self.start[1] + self.y)
        pygame.draw.circle(screen, self.color, self.circle, self.radius)

        if abs(self.circle[0] - center[0]) + self.radius > abs(rect[0][0] - center[0]):
            self.x_direction = self.x_direction * -1
            self.x_i = 0

        if self.x_i == 1:
            self.x_speed = random.randint(1, self.random_factor)
            # self.x_speed += 1


        if abs(self.circle[1] - center[1]) + self.radius > abs(rect[0][1] - center[1]):
            self.y_direction = self.y_direction * -1
            self.y_i = 0

        i = 0

        for corner in corners:
            corner_x = corner[0][0]
            corner_y = corner[1][0]
            corner_x_extreme = corner[0][1]
            corner_y_extreme = corner[1][1]
            if i == 0:  # Corner 200, 200
                if corner_x >= self.circle[0] - self.radius and self.circle[1] - self.radius <= corner_y_extreme:
                    corner_values.pop(i)
                    corner_values.insert(i, self.color)
                if self.circle[0] - self.radius <= corner_x_extreme and corner_y >= self.circle[1] - self.radius:
                    corner_values.pop(i)
                    corner_values.insert(i, self.color)
            if i == 1:
                if corner_x >= self.circle[0] - self.radius and self.circle[1] + self.radius >= corner_y_extreme:
                    corner_values.pop(i)
                    corner_values.insert(i, self.color)
                if self.circle[0] - self.radius <= corner_x_extreme and corner_y <= self.circle[1] + self.radius:
                    corner_values.pop(i)
                    corner_values.insert(i, self.color)

            if i == 2:
                if corner_x <= self.circle[0] + self.radius and self.circle[1] - self.radius <= corner_y_extreme:
                    corner_values.pop(i)
                    corner_values.insert(i, self.color)
                if self.circle[0] + self.radius >= corner_x_extreme and corner_y >= self.circle[1] - self.radius:
                    corner_values.pop(i)
                    corner_values.insert(i, self.color)
            if i == 3:
                if corner_x <= self.circle[0] + self.radius and self.circle[1] + self.radius >= corner_y_extreme:
                    corner_values.pop(i)
                    corner_values.insert(i, self.color)
                if self.circle[0] + self.radius >= corner_x_extreme and corner_y <= self.circle[1] + self.radius:
                    corner_values.pop(i)
                    corner_values.insert(i, self.color)
            i += 1

        if self.y_i == 1:
            self.y_speed = random.randint(1, self.random_factor)
            # self.y_speed += 1

        # Attempted for use in calculating ball collisions with each other
        # if self.n_i == 1:
        #     self.y_direction = self.y_direction * -1
        #     self.x_direction = self.x_direction * -1

        self.x += (self.x_speed * self.x_direction)
        self.y += (self.y_speed * self.y_direction)
        self.x_i += 1
        self.y_i += 1
        self.n_i += 1


ball_colors = (red, white, yellow, orange, (22, 219, 91), (173, 98, 252), (255, 0, 208), (0, 247, 255), (143, 250, 10), (123, 2, 241), red, red, orange, orange, white, white, orange, yellow, red, red, red, orange, white, orange, orange, red, orange, yellow, white, white)
ball_colors = []

number_balls = 10

random_ball_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(number_balls)]

ball_radius = 20
ball_collisions = True
Balls = [Ball(random_ball_colors[i], ball_radius) for i in range(number_balls)]
counters = []
for i in range(number_balls):
    counters.append([])
for c in counters:
    for co in counters:
        c.append([0])


Ball_1 = Ball(red, 10)
Ball_2 = Ball(white, 10)
Ball_3 = Ball(yellow, 10)
Ball_4 = Ball(orange, 10)
Ball_5 = Ball((22, 219, 91), 10)
Ball_6 = Ball((173, 98, 252), 10)
Ball_7 = Ball((255, 0, 208), 10)
Ball_8 = Ball((0, 247, 255), 10)

frame = 0
while True:
    passed_time = clock.tick(100) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if ball_collisions:
                    ball_collisions = False
                else:
                    ball_collisions = True

    screen.fill((blue))
    pygame.draw.rect(screen, black, rect, 8)

    x_Ball_ranges = []
    y_Ball_ranges = []
    for Ball in Balls:
        Ball.cycle()
        x_Ball_ranges.append([Ball.circle[0]-Ball.radius, Ball.circle[0]+Ball.radius])
        y_Ball_ranges.append([Ball.circle[1]-Ball.radius, Ball.circle[1]+Ball.radius])
    # Ball Collision- Comment out to go back to normal- working version
    if ball_collisions:
        for i_Ball in range(0, len(Balls)):
            for i_Ball_2 in range(i_Ball+1, len(Balls)):
                if counters[i_Ball][i_Ball_2][0] == 0:
                    if x_Ball_ranges[i_Ball_2][0]<= x_Ball_ranges[i_Ball][0] <= x_Ball_ranges[i_Ball_2][1] or x_Ball_ranges[i_Ball_2][0]<= x_Ball_ranges[i_Ball][1] <= x_Ball_ranges[i_Ball_2][1]:
                        if y_Ball_ranges[i_Ball_2][0]<= y_Ball_ranges[i_Ball][0] <= y_Ball_ranges[i_Ball_2][1] or y_Ball_ranges[i_Ball_2][0]<= y_Ball_ranges[i_Ball][1] <= y_Ball_ranges[i_Ball_2][1]:

                            counters[i_Ball][i_Ball_2] = [Balls[i_Ball].radius+1]

                            if Balls[i_Ball].x_direction == Balls[i_Ball_2].x_direction:
                                Balls[i_Ball].x_direction = Balls[i_Ball].x_direction * -1
                            else:
                                Balls[i_Ball].x_direction = Balls[i_Ball].x_direction * -1
                                Balls[i_Ball_2].x_direction = Balls[i_Ball_2].x_direction * -1

                            if Balls[i_Ball].y_direction == Balls[i_Ball_2].y_direction:
                                Balls[i_Ball].y_direction = Balls[i_Ball].y_direction * -1
                            else:
                                Balls[i_Ball].y_direction = Balls[i_Ball].y_direction * -1
                                Balls[i_Ball_2].y_direction = Balls[i_Ball_2].y_direction * -1
                else:
                    counters[i_Ball][i_Ball_2][0] = counters[i_Ball][i_Ball_2][0]-1

    corner_i = 0
    for corner_color in corner_values:
        pygame.draw.line(screen, corner_color, corner_points[corner_i], corner_points_x_offsets[corner_i], 7)
        pygame.draw.line(screen, corner_color, corner_points[corner_i], corner_points_y_offsets[corner_i], 7)
        corner_i += 1

    frame += 1

    pygame.display.flip()

