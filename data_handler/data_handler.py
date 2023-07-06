import pickle
from config import *


class Data_Handler:
    def __init__(self):
        self.reds_data = self.load_reds_data()
        self.nutrients_data = self.load_nutrients_data()

    @staticmethod
    def load_reds_data():

        try:
            with open('database/reds_data.bin', 'rb') as file:
                reds_data = pickle.load(file)
            return reds_data

        except Exception as ex:
            print(ex)

    @staticmethod
    def load_nutrients_data():

        try:
            with open('database/nutrients_data.bin', 'rb') as file:
                nutrients_data = pickle.load(file)
            return nutrients_data

        except Exception as ex:
            print(ex)

    def print_reds_data(self):
        for k, v in self.reds_data.items():
            print(k, ':', v)

    def print_nutrients_data(self):
        for k, v in self.nutrients_data.items():
            print(k, ':', v)

    def population(self):
        red_y, iteration_x = list(), list()

        for itr, red in self.reds_data.items():
            iteration_x.append(itr)
            red_y.append(len(red))

        return iteration_x, red_y

    def nutrients(self):
        n_y, i_x = list(), list()

        for i, n in self.nutrients_data.items():
            i_x.append(i)
            n_y.append(n)

        return i_x, n_y




