from config import *
from data_handler.data_handler import Data_Handler
import matplotlib.pyplot as plt


class Plots_Constructor:
    def __init__(self):
        self.data_handler = Data_Handler()

        self.fig, self.axs = plt.subplots(nrows=2, ncols=3, figsize=(15, 7.4))


    def population_nutrients_plots(self):
        x, y = self.data_handler.population()

        self.axs[0, 0].plot(x, y, color=(1, 0, 0))
        self.axs[0, 0].grid(True)
        self.axs[0, 0].set_xlabel('Iteration')
        self.axs[0, 0].set_ylabel('Reds amount')

        x1, y1 = self.data_handler.nutrients()
        self.axs[1, 0].plot(x1, y1, color=(0, 1, 0))
        self.axs[1, 0].grid(True)
        self.axs[1, 0].set_xlabel('Iteration')
        self.axs[1, 0].set_ylabel('Nutrients amount')

        plt.show()



