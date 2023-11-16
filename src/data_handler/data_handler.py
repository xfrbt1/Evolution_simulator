import pickle
from src.config import *


class Data_Handler:
    def __init__(self):
        self.reds_data = self.load_reds_data()
        self.nutrients_data = self.load_nutrients_data()

    @staticmethod
    def load_reds_data():

        try:
            with open('src/database/reds_data.bin', 'rb') as file:
                reds_data = pickle.load(file)
            return reds_data

        except Exception as ex:
            print(ex)

    @staticmethod
    def load_nutrients_data():

        try:
            with open('src/database/nutrients_data.bin', 'rb') as file:
                nutrients_data = pickle.load(file)
            return nutrients_data

        except Exception as ex:
            print(ex)

    def average_reds_amount(self) -> float:
        s = 0
        n = 0
        for red_list in self.reds_data.values():
            n += 1
            s += len(red_list)

        return s / n

    def population(self) -> tuple[list, list]:
        red_y, iteration_x = list(), list()

        for itr, red in self.reds_data.items():
            iteration_x.append(itr)
            red_y.append(len(red))

        return iteration_x, red_y

    def nutrients(self) -> tuple[list, list]:
        n_y, i_x = list(), list()

        for i, n in self.nutrients_data.items():
            i_x.append(i)
            n_y.append(n)

        return i_x, n_y

    def generations_list(self) -> list:
        generations = list()

        for entity_list in self.reds_data.values():
            for entity in entity_list:
                if (entity[9], entity[10]) not in generations:
                    generations.append((entity[9], entity[10]))

        return generations

    def generations_characteristics(self) -> dict:
        gen_crt = dict()

        for entity_list in self.reds_data.values():
            for entity in entity_list:
                if entity[10] not in gen_crt:
                    gen_crt[entity[10]] = (entity[6],
                                           entity[7],
                                           entity[8])

        return gen_crt

    def generations_colors(self) -> dict:
        gen_colors = dict()

        for entity_list in self.reds_data.values():
            for entity in entity_list:
                if entity[10] not in gen_colors.keys():
                    gen_colors[entity[10]] = (entity[11][0] / 255, entity[11][1] / 255, entity[11][2] / 255)

        return gen_colors

    def generations_weight(self) -> dict:
        gen_amount = dict()

        for entity_list in self.reds_data.values():
            for entity in entity_list:
                if entity[10] not in gen_amount.keys():
                    gen_amount[entity[10]] = 0
                else:
                    gen_amount[entity[10]] += 1

        return gen_amount

    def generations_dictionary_graph(self) -> dict:

        generations_list = self.generations_list()
        graph = dict()

        for gen, gen_scr in generations_list:
            if gen_scr not in graph.keys():
                graph[gen_scr] = list()

        for gen_parents in graph.keys():
            for gen, gen_scr in generations_list:
                if gen_parents in gen_scr and len(gen_scr) == len(gen_parents) + 1:
                    graph[gen_parents].append(gen_scr)

        return graph

    def top_generations(self, n: int) -> tuple[list, list, list]:
        scrs = list()
        weights = list()
        colors = list()

        gen_color = self.generations_colors()
        gen_weight = self.generations_weight()

        top_gen = sorted(gen_weight.items(), key=lambda x: x[1], reverse=True)[:n]

        for gen in top_gen:
            scrs.append(gen[0])
            weights.append(gen[1])
            colors.append(gen_color[gen[0]])

        return scrs, weights, colors

    def top_generations_statistics(self, n: int):
        gen_ch = self.generations_characteristics()
        gen_weight = self.generations_weight()

        top_gen = sorted(gen_weight.items(), key=lambda x: x[1], reverse=True)[:n]

        for gen in top_gen:
            print("\n_____________________________________")
            print(f"GENERATION SCRIPT: {gen[0]}")
            print(f"GENERATION WEIGHT: {gen[1]}")
            print(f"SPEED: {round(gen_ch[gen[0]][0], 2)}")
            print(f"SIZE: {round(gen_ch[gen[0]][1], 2)}")
            print(f"SATURATION: {gen_ch[gen[0]][2]}")











