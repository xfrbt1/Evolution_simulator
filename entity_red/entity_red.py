import time
import pygame as pg
from config import *


class REDS:
    entity_x = 100  # 0
    entity_y = 100  # 1
    target_x = None  # 2
    target_y = None  # 3
    target_sum = None  # 4
    energy = 99  # 5
    speed = 1  # 6
    capture_radius = 1  # 7


class Red_Entity:
    def __init__(self, state):
        self.state = state
        self.nutrients = state.nutrients

        self.red_entity_array = list()
        self.dead_red_array = list()
        self.append_progenitor()

    def append_progenitor(self):
        self.red_entity_array.append([REDS.entity_x,
                                      REDS.entity_y,
                                      REDS.target_x,
                                      REDS.target_y,
                                      REDS.target_sum,
                                      REDS.energy,
                                      REDS.speed,
                                      REDS.capture_radius])

    def choose_target(self):
        for entity in self.red_entity_array:
            for nutrient in self.nutrients.nutrient_array:

                if entity[4] is None or (abs(entity[0] - nutrient[0]) + abs(entity[1] - nutrient[1])) < entity[4]:
                    entity[2] = nutrient[0]
                    entity[3] = nutrient[1]
                    entity[4] = (abs(entity[0] - nutrient[0]) + abs(entity[1] - nutrient[1]))

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

                if abs(self.red_entity_array[entity][0] - self.nutrients.nutrient_array[nutrient][0]) <= \
                        self.red_entity_array[entity][7]:
                    if abs(self.red_entity_array[entity][1] - self.nutrients.nutrient_array[nutrient][1]) <= \
                            self.red_entity_array[entity][7]:

                        if self.nutrients.nutrient_array[nutrient] not in nutrients_delete:
                            nutrients_delete.append(self.nutrients.nutrient_array[nutrient])
                            self.increment_energy(entity)
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

    def increment_energy(self, entity_index):
        self.red_entity_array[entity_index][5] += 33

    def decrement_energy(self):
        for entity in self.red_entity_array:
            entity[5] -= 1

    def check_death(self):
        delete_list = list()
        for entity in self.red_entity_array:
            if entity[5] <= 0:
                delete_list.append(entity)

        for entity in delete_list:
            self.red_entity_array.remove(entity)
            self.dead_red_array.append(entity)

    def make_division(self):
        division_list = list()

        for entity in self.red_entity_array:
            if entity[5] >= 100:
                division_list.append(entity)

        for entity in division_list:
            self.red_entity_array.append([entity[0]+10,
                                          entity[1]+10,
                                          None,
                                          None,
                                          None,
                                          60,
                                          1,
                                          1])
            self.red_entity_array.append([entity[0]-10,
                                          entity[1]-10,
                                          None,
                                          None,
                                          None,
                                          60,
                                          1,
                                          1])
            self.red_entity_array.remove(entity)



    def update(self):

        self.check_nutrients_existence()
        self.choose_target()
        self.check_collisions()
        self.reds_eat_nutrients()
        self.make_division()
        self.move()
        self.decrement_energy()

        self.check_death()


    def draw_red_array(self):
        for i in self.red_entity_array:
            pg.draw.circle(self.state.screen, color_red,
                           (i[0], i[1]), 5)

    def draw_dead_reds(self):
        for i in self.dead_red_array:
            pg.draw.circle(self.state.screen, color_gray,
                           (i[0], i[1]), 4)

    def draw(self):
        self.draw_dead_reds()
        self.draw_red_array()

    @property
    def get_amount(self):
        return len(self.red_entity_array)
