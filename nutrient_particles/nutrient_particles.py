import random
import pygame as pg

from config import *


class Nutrient:
    def __init__(self, state):

        self.nutrient_array = list()
        self.state = state

    def new_particle(self):
        if self.state.clock.tick(FPS) == 1:
            self.nutrient_array.append([random.randint(0, WIDTH), random.randint(0, HEIGHT)])

    @property
    def get_amount(self):
        return len(self.nutrient_array)

    def update(self):
        self.new_particle()

    def draw(self):
        for i in self.nutrient_array:
            pg.draw.circle(self.state.screen, color_green_d,
                           (i[0], i[1]), 2)

        print(self.nutrient_array)


