import pygame as pg
import sys

from config import *
from nutrient_particles.nutrient_particles import Nutrient
from entity_red.entity_red import Red_Entity


class Simulation_State:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        pg.init()

        self.iteration_step = 0
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.new_state()

    def new_state(self):
        self.nutrients = Nutrient(self)
        self.red_entities = Red_Entity(self)

    def update(self):
        pg.display.set_caption(f"{CAPTION}")
        pg.display.flip()
        self.clock.tick(FPS)

        self.nutrients.update()
        self.red_entities.update()

        self.iteration_step += 1

    def draw(self):
        self.screen.fill(color_white)
        self.nutrients.draw()
        self.red_entities.draw()

    def create_log(self):
        pass

    @staticmethod
    def check_event():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def print_data(self):
        if self.iteration_step % 100 == 0:
            print('iteration:', self.iteration_step)
            print('fps: ', round(self.clock.get_fps(), 2))
            print(self.red_entities)
            print(self.nutrients)
            print('_____________________')

    def run(self):
        while True:
            self.update()
            self.draw()
            self.check_event()
            self.print_data()







