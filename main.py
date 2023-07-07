import time

from simulation_state.simulation_state import Simulation_State
from plots_constructor.plots_constructor import Plots_Constructor

if __name__ == '__main__':
    print("\033[H\033[J")

    # simulation_state = Simulation_State()
    #
    # simulation_state.run()
    #
    # simulation_state.save_data()

    plots_constructor = Plots_Constructor()

    plots_constructor.population_nutrients_plots()

    plots_constructor.data_handler.top_generations_statistics(5)

    plots_constructor.generations_graph(None)

    plots_constructor.top_generations_bar(5)
















