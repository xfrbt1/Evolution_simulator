import time
import pygame as pg
from config import *


class REDS:
    entity_x = 10  # 0
    entity_y = 10  # 1
    target_x = None  # 2
    target_y = None  # 3
    target_sum = None  # 4
    energy = 0  # 5
    speed = 2  # 6


class Red_Entity:
    def __init__(self, state):
        self.state = state
        self.nutrients = state.nutrients

        self.red_entity_array = list()
        self.append_progenitor()

    def append_progenitor(self):
        self.red_entity_array.append([REDS.entity_x,
                                      REDS.entity_y,
                                      REDS.target_x,
                                      REDS.target_y,
                                      REDS.target_sum,
                                      REDS.energy,
                                      REDS.speed])

        self.red_entity_array.append([REDS.entity_x+100,
                                      REDS.entity_y+100,
                                      REDS.target_x,
                                      REDS.target_y,
                                      REDS.target_sum,
                                      REDS.energy,
                                      REDS.speed+2])

    def choose_target(self):
        for entity in self.red_entity_array:
            if entity[2] is None or entity[3] is None and len(self.nutrients.nutrient_array) > 0:
                for nutrient in self.nutrients.nutrient_array:
                    xd = abs(entity[0] - nutrient[0])
                    yd = abs(entity[1] - nutrient[1])
                    s = xd + yd
                    if entity[4] is None or s < entity[4]:
                        entity[2] = nutrient[0]
                        entity[3] = nutrient[1]
                        entity[4] = s

    def move(self):
        for entity in self.red_entity_array:
            if (entity[3] or entity[2]) is None:
                continue
            if entity[0] < entity[2]:
                entity[0] += entity[6]
            if entity[1] < entity[3]:
                entity[1] += entity[6]
            if entity[0] > entity[2]:
                entity[0] -= entity[6]
            if entity[1] > entity[3]:
                entity[1] -= entity[6]

    def check_nutrients_existence(self):
        for entity in self.red_entity_array:
            if (entity[2], entity[3]) not in self.nutrients.nutrient_array:
                entity[2] = None
                entity[3] = None
                entity[4] = None

    # def check_nutrients_reds_match(self):
    #
    #     for entity in self.red_entity_array:
    #         indexes_del = list()
    #         for i in range(len(self.nutrients.nutrient_array)):
    #             if abs(entity[0] - self.nutrients.nutrient_array[i][0]) < entity[6] and\
    #                     abs(entity[1] - self.nutrients.nutrient_array[i][1]) < entity[6]:
    #
    #                 entity[2] = None
    #                 entity[3] = None
    #                 entity[4] = None
    #                 entity[5] += 1
    #
    #                 if i not in indexes_del:
    #                     indexes_del.append(i)
    #
    #                 for j in indexes_del:
    #                     self.nutrients.nutrient_array.pop(j)

    def increment_energy(self, i):
        pass

    def decrement_energy(self):
        pass

    def make_division(self):
        pass

    def update(self):
        self.check_nutrients_existence()
        self.choose_target()
        self.move()
        print(self.red_entity_array)

    def draw(self):
        for i in self.red_entity_array:
            pg.draw.circle(self.state.screen, color_red_d,
                           (i[0], i[1]), 5)

    @property
    def get_amount(self):
        return len(self.red_entity_array)
