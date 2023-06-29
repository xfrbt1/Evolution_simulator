import random
import pygame as pg
import pygame.key

from config import *


class Nutrient:
    def __init__(self, state):

        self.state = state
        self.nutrient_array = list()
        self.first_nutrients()

    def first_nutrients(self):
        self.nutrient_array.append((200, 200))
        self.nutrient_array.append((600, 500))

    def new_particle_t(self):
        if int((pg.time.get_ticks() - self.state.start_time) / 1000) % 10 == 0:
            self.nutrient_array.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    def new_particle_p(self):
        keys = pygame.key.get_pressed()
        if keys[pg.K_0]:
            self.nutrient_array.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    def update(self):
        self.new_particle_p()
        self.new_particle_t()

    def draw(self):
        for i in self.nutrient_array:
            pg.draw.circle(self.state.screen, color_green_d,
                           (i[0], i[1]), 3)

    @property
    def get_amount(self):
        return len(self.nutrient_array)



