import os
import pickle
import threading
import pygame as pg

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
        self.running = True

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.new_state()

    def new_state(self):
        self.nutrients = Nutrient(self)
        self.reds = Red_Entity(self)

    def update(self):
        pg.display.set_caption(f"{CAPTION}")
        pg.display.flip()
        self.clock.tick(FPS)

        self.nutrients.update()
        self.reds.update()

        self.iteration_step += 1

    def draw(self):
        self.screen.fill(color_white)
        self.nutrients.draw()
        self.reds.draw()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()

    def data_collect(self):
        self.reds.data_collect()
        self.nutrients.data_collect()

    def run(self):
        while self.running:
            threading.Thread(target=self.data_collect()).start()
            self.update()
            self.draw()
            self.check_event()

    def end_simulation(self):
        print('END')

    def save_data(self):
        self.nutrients.save_data()
        self.reds.save_data()







