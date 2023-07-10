import pickle
import random

import pygame as pg
from copy import deepcopy

from config import *


class RED:
    entity_x = WIDTH // 2  # 0
    entity_y = HEIGHT // 2  # 1
    target_x = None  # 2
    target_y = None  # 3
    target_sum = None  # 4
    energy = 99  # 5
    speed = 0.5  # 6
    size = 4  # 7
    saturation = 30  # 8
    generation_id = 0  # 9
    generation_id_str = 'p'  # 10
    color = (255, 0, 0)  # 11


class Red_Entity:
    def __init__(self, state):
        self.state = state
        self.nutrients = state.nutrients

        self.reds_array = list()
        self.dead_reds_array = list()
        self.append_progenitor()

        self.reds_data = dict()

    def append_progenitor(self):
        self.reds_array.append([
            RED.entity_x,
            RED.entity_y,
            RED.target_x,
            RED.target_y,
            RED.target_sum,
            RED.energy,
            RED.speed,
            RED.size,
            RED.saturation,
            RED.generation_id,
            RED.generation_id_str,
            RED.color
        ])

    def choose_target(self):

        for entity in self.reds_array:
            if entity[4] is None:
                for nutrient in self.nutrients.nutrients_array:
                    target_sum = (abs(entity[0] - nutrient[0]) + abs(entity[1] - nutrient[1]))
                    if entity[4] is None or target_sum < entity[4]:
                        entity[2] = nutrient[0]
                        entity[3] = nutrient[1]
                        entity[4] = target_sum

    def move(self):

        for entity in self.reds_array:
            if (entity[3] or entity[2]) is None:
                continue
            if entity[0] - entity[2] < entity[7]:
                entity[0] += entity[6]
            if entity[0] - entity[2] > entity[7]:
                entity[0] -= entity[6]
            if entity[1] - entity[3] < entity[7]:
                entity[1] += entity[6]
            if entity[1] - entity[3] > entity[7]:
                entity[1] -= entity[6]

            entity[5] -= 0.5

    def check_nutrients_existence(self):

        for entity in self.reds_array:
            if (entity[2], entity[3]) not in self.nutrients.nutrients_array:
                entity[2] = None
                entity[3] = None
                entity[4] = None

    def set_target_none(self, i):
        self.reds_array[i][2] = None
        self.reds_array[i][3] = None
        self.reds_array[i][4] = None

    def check_collisions(self):
        for entity_i in self.reds_array:
            for entity_j in self.reds_array:
                if entity_i == entity_j:
                    continue
                if abs(entity_i[0]-entity_j[0]) < entity_j[7] + entity_i[7] and abs(entity_i[1]-entity_j[1]) < entity_j[7] + entity_i[7]:
                    self.reds_array.remove(entity_i)
                    break

    def reds_eat_nutrients_(self):
        for entity in range(len(self.reds_array)):
            for nutrient in range(len(self.nutrients.nutrients_array)):

                if abs(self.reds_array[entity][0] - self.nutrients.nutrients_array[nutrient][0]) <= \
                        self.reds_array[entity][7]:
                    if abs(self.reds_array[entity][1] - self.nutrients.nutrients_array[nutrient][1]) <= \
                            self.reds_array[entity][7]:
                        self.nutrients.nutrients_array.remove(self.nutrients.nutrients_array[nutrient])
                        break

    def reds_eat_nutrients(self):
        for entity in self.reds_array:
            if entity[2] is not None:
                if abs(entity[0] - entity[2]) <= entity[7] and abs(entity[1] - entity[3]) <= entity[7]:
                    if (entity[2], entity[3]) in self.nutrients.nutrients_array:
                        self.nutrients.nutrients_array.remove((entity[2], entity[3]))

                        entity[5] += entity[8]

    def decrement_energy(self):

        for entity in self.reds_array:
            entity[5] -= 1

    def check_death(self):

        for entity in self.reds_array:
            if entity[5] <= 0:
                self.reds_array.remove(entity)
                self.dead_reds_array.append((entity[0], entity[1], entity[7]))

    def clear_dead_list(self):

        if self.state.iteration_step % 500 == 0:
            self.dead_reds_array.clear()

    def make_division(self):

        for entity in self.reds_array:
            if entity[5] >= 100:
                mutation = random.randint(0, MUTATION_FREQ)
                self.append_after_division(entity, mutation)
                self.reds_array.remove(entity)

    def append_after_division(self, entity, mutate):
        if mutate == 100:
            field = random.randint(6, 8)
            if field == 7:
                modification = random.choice([1, 3, -1])
            elif field == 6:
                modification = random.choice([0.2, -0.2, -0.4])
            else:
                modification = random.choice([4, -2])

            entity[field] += modification
            entity[9] += 1
            entity[10] += random.choice(ALF)
            entity[11] = random.choice(COLORS)

        x = entity[0]
        y = entity[1]
        speed = entity[6]
        size = entity[7]
        saturation = entity[8]
        color = entity[11]

        self.reds_array.append([x+entity[7], y-entity[7], None, None, None, 60, speed, size, saturation, entity[9], entity[10], color])
        self.reds_array.append([x-entity[7], y+entity[7], None, None, None, 60, speed, size, saturation, entity[9], entity[10], color])

    def update(self):
        self.check_nutrients_existence()
        self.choose_target()
        self.move()
        self.reds_eat_nutrients()
        self.make_division()

        self.check_death()
        self.clear_dead_list()

    def draw_red_array(self):

        for i in self.reds_array:

            pg.draw.circle(self.state.screen, i[11],
                           (i[0], i[1]), i[7]+2)

    def draw_dead_reds(self):

        for i in self.dead_reds_array:
            pg.draw.circle(self.state.screen, color_gray_d,
                           (i[0], i[1]), i[2])

    def draw(self):
        self.draw_dead_reds()
        self.draw_red_array()

    @property
    def get_red_amount(self):
        return len(self.reds_array)

    @property
    def get_dead_amount(self):
        return len(self.dead_reds_array)

    def get_red_list(self):
        return self.reds_array

    def __str__(self):
        return f"REDS AMOUNT: {self.get_red_amount}\nDEAD AMOUNT: {self.get_dead_amount}"

    def data_collect(self):
        if self.state.iteration_step % 100 == 0:
            self.reds_data[self.state.iteration_step] = deepcopy(self.reds_array)

    def save_data(self):

        try:
            with open('database/reds_data.bin', 'wb') as file:
                pickle.dump(self.reds_data, file)

        except Exception as ex:
            print(ex)
