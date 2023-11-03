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
        self.font = pg.font.Font(None, TXT_SIZE)

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
            elif event.type == pg.MOUSEBUTTONDOWN:
                print(pg.mouse.get_pos())

    def data_collect(self):
        self.reds.data_collect()
        self.nutrients.data_collect()

    def txt_info(self):
        pg.draw.rect(self.screen, color_white, TXT_RECT_CORDS)
        itr_step_txt = self.font.render(f'itr: {self.iteration_step}', True, color_black)
        fps_txt = self.font.render(f'fps: {int(self.clock.get_fps())}', True, color_black)
        reds_txt = self.font.render(f'reds: {self.reds.get_red_amount}', True, color_black)
        nutrients_txt = self.font.render(f'nutr: {self.nutrients.get_amount}', True, color_black)
        self.screen.blit(itr_step_txt, (TXT_X, 10))
        self.screen.blit(fps_txt, (TXT_X, 30))
        self.screen.blit(reds_txt, (TXT_X, 50))
        self.screen.blit(nutrients_txt, (TXT_X, 70))

    def run(self):
        while self.running:
            threading.Thread(target=self.data_collect()).start()
            self.update()
            self.draw()
            self.txt_info()
            self.check_event()

    def save_data(self):
        self.nutrients.save_data()
        self.reds.save_data()

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"{self.iteration_step}:{self.reds}"

    @staticmethod
    def end_simulation():
        print('END')







