from src.config import *
from src.data_handler.data_handler import Data_Handler
import matplotlib.pyplot as plt
import networkx as nx


class Plots_Constructor:
    def __init__(self):
        self.data_handler = Data_Handler()

    def population_nutrients_plots(self):
        x, y = self.data_handler.population()
        fig, axs = plt.subplots(nrows=2)
        axs[0].plot(x, y, color=(1, 0, 0))
        axs[0].grid(True)
        axs[0].set_xlabel("Iteration")
        axs[0].set_ylabel("Reds amount")

        x1, y1 = self.data_handler.nutrients()
        axs[1].plot(x1, y1, color=(0, 1, 0))
        axs[1].grid(True)
        axs[1].set_xlabel("Iteration")
        axs[1].set_ylabel("Nutrients amount")

        plt.show()

    def generations_graph(self, n=-2):
        graph = self.data_handler.generations_dictionary_graph()
        gen_colors = self.data_handler.generations_colors()

        new_names = {}
        for node in graph.keys():
            new_names[node] = node[n:]

        nx_graph = nx.Graph(graph)

        for node, edges in graph.items():
            for edge in edges:
                nx_graph.add_edge(node, edge)

        nx.draw(
            nx_graph,
            node_color=[gen_colors[node] for node in nx_graph.nodes()],
            with_labels=True,
            font_size=10,
            node_size=150,
            labels=new_names,
        )

        plt.show()

    def top_generations_bar(self, n=5):

        fig, ax = plt.subplots()

        x, y, colors = self.data_handler.top_generations(n)
        ax.bar(x, y, color=colors)
        for i in range(len(x)):
            plt.text(x[i], y[i], str(y[i]), ha="center")

        ax.set_xlabel("Generations scripts")
        ax.set_ylabel("Generations weights")

        plt.show()

    def top_generations_statistics(self, n=5):
        return self.data_handler.top_generations_statistics(n)
