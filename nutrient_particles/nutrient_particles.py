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
        for i in range(FIRST_NUTRIENTS_AMOUNT):
            self.nutrient_array.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    def new_particle_timer(self):
        if self.state.iteration_step % NUTRIENT_QUANTITY_DIVISOR == 0:
            self.nutrient_array.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    def new_particle_press(self):
        keys = pygame.key.get_pressed()
        if keys[pg.K_0]:
            for i in range(50):
                self.nutrient_array.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    def update(self):
        self.new_particle_press()
        self.new_particle_timer()

    def draw(self):
        for i in self.nutrient_array:
            pg.draw.circle(self.state.screen, color_green_d,
                           (i[0], i[1]), 3)

    @property
    def get_amount(self):
        return len(self.nutrient_array)

    def __str__(self):
        return f"nutrients amount: {self.get_amount}"



