from random import randint, choice
import time
import os

TERMINAL_WIDTH = 80
TERMINAL_HEIGHT = 20
STAR_COUNT = 150

class Star:
    def __init__(self):
        self.x = randint(0, TERMINAL_WIDTH - 1)
        self.y = randint(0, TERMINAL_HEIGHT - 1)
        self.size = choice([1, 2, 3])
        self.speed = choice([0.1, 0.2, 0.3])
        self.char = choice(["*", ".", "o", "+", "x", "#", "&"])
        self.color = choice([31, 32, 33, 34, 35, 36])

    def fall(self):
        self.y += self.size
        if self.y >= TERMINAL_HEIGHT:
            self.y = 0
            self.x = randint(0, TERMINAL_WIDTH - 1)
            self.size = choice([1, 2, 3])
            self.speed = choice([0.1, 0.2, 0.3])

    def get_display(self):
        return f"\033[{self.color}m{self.char}\033[0m"

stars = [Star() for _ in range(STAR_COUNT)]

def draw():
    screen = [[" " for _ in range(TERMINAL_WIDTH)] for _ in range(TERMINAL_HEIGHT)]
    for star in stars:
        if 0 <= star.y < TERMINAL_HEIGHT and 0 <= star.x < TERMINAL_WIDTH:
            if star.size == 1:
                screen[star.y][star.x] = star.get_display()
            elif star.size == 2:
                screen[star.y][star.x] = star.get_display()
                if star.x + 1 < TERMINAL_WIDTH:
                    screen[star.y][star.x + 1] = star.get_display()
                if star.y + 1 < TERMINAL_HEIGHT:
                    screen[star.y + 1][star.x] = star.get_display()
            elif star.size == 3:
                screen[star.y][star.x] = star.get_display()
                if star.x + 1 < TERMINAL_WIDTH:
                    screen[star.y][star.x + 1] = star.get_display()
                if star.y + 1 < TERMINAL_HEIGHT:
                    screen[star.y + 1][star.x] = star.get_display()
                if star.x - 1 >= 0:
                    screen[star.y][star.x - 1] = star.get_display()
                if star.y - 1 >= 0:
                    screen[star.y - 1][star.x] = star.get_display()
    return "\n".join(["".join(row) for row in screen])

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(draw())
    for star in stars:
        star.fall()
    time.sleep(0.1)
