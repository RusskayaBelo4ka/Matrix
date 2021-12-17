import pygame
import sys
import random


class Number:

    FONT = "Elfboyclassic.ttf"
    SIZE_FONT = 25
    COLOR = (0, 255, 0)
    COLOR_LAST = (190, 245, 116)

    def __init__(self, x, y, speed):
        self.elements = [i for i in range(100)]
        self.font = pygame.font.Font(self.FONT, self.SIZE_FONT)
        self.element = self.font.render(str(random.choice(self.elements)), False, self.COLOR)
        self.x, self.y = x, y
        self.speed = speed
        self.color = self.COLOR

    def move(self):
        self.y += self.speed
        if self.y > SIZE_SCREEN[1]:
            self.y = -10

    def change(self):
        self.element = self.font.render(str(random.choice(self.elements)), False, self.color)

    def render(self):
        self.element.set_alpha(222)
        screen.blit(self.element, (self.x, self.y))


pygame.init()

SIZE_SCREEN = (1200, 1200)
FPS = 50

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption('Matrix')


coord_x = [i for i in range(20, SIZE_SCREEN[0]-20, 60)]
coord_y = [i for i in range(0, SIZE_SCREEN[1]//2, 20)]
numbers = []

for i in coord_x:
    spd = random.randint(4, 12)
    for z in coord_y:
        numbers.append(Number(i, z, spd))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    [i.render() for i in numbers]
    [i.move() for i in numbers]
    for i in numbers[len(coord_y)-1::len(coord_y)]:
        i.color = i.COLOR_LAST
        print(len(coord_y))
    random.choice(numbers).change()
    pygame.display.update()
    clock.tick(FPS)
