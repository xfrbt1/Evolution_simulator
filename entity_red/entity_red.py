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
                                      REDS.speed])

        self.red_entity_array.append([REDS.entity_x+200,
                                      REDS.entity_y+300,
                                      REDS.target_x,
                                      REDS.target_y,
                                      REDS.target_sum,
                                      REDS.energy,
                                      REDS.speed])

        self.red_entity_array.append([REDS.entity_x-100,
                                      REDS.entity_y+100,
                                      REDS.target_x,
                                      REDS.target_y,
                                      REDS.target_sum,
                                      REDS.energy,
                                      REDS.speed])

    def choose_target(self):
        for entity in self.red_entity_array:
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

    def set_target_none(self, i):
        self.red_entity_array[i][2] = None
        self.red_entity_array[i][3] = None
        self.red_entity_array[i][4] = None

    def reds_eat_nutrients(self):
        nutrients_delete = list()

        for entity in range(len(self.red_entity_array)):
            for nutrient in range(len(self.nutrients.nutrient_array)):

                if abs(self.red_entity_array[entity][0] - self.nutrients.nutrient_array[nutrient][0]) <= 2:
                    if abs(self.red_entity_array[entity][1] - self.nutrients.nutrient_array[nutrient][1]) <= 2:

                        if self.nutrients.nutrient_array[nutrient] not in nutrients_delete:
                            nutrients_delete.append(self.nutrients.nutrient_array[nutrient])
                            self.red_entity_array[entity][5] += 1
                            print(*self.red_entity_array)
                            print(*nutrients_delete)
                            break

        for i in nutrients_delete:
            self.nutrients.nutrient_array.remove(i)

    def check_collisions(self):
        for entity_i in self.red_entity_array:
            for entity_j in self.red_entity_array:

                if entity_i is entity_j:
                    continue
                if entity_i[0] == entity_j[0]:
                    if entity_i[1] == entity_j[1]:
                        entity_i[0] += 10
                        entity_i[1] += 10
                        entity_j[0] -= 10
                        entity_j[1] -= 10

    def increment_energy(self):
        pass

    def decrement_energy(self):
        pass

    def make_division(self):
        pass

    def update(self):
        self.choose_target()
        self.check_nutrients_existence()
        self.reds_eat_nutrients()
        self.check_collisions()
        self.move()

    def draw(self):
        for i in self.red_entity_array:
            pg.draw.circle(self.state.screen, color_red_d,
                           (i[0], i[1]), 5)

    @property
    def get_amount(self):
        return len(self.red_entity_array)
