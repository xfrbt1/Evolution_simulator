import time

from simulation_state.simulation_state import Simulation_State
from plots_constructor.plots_constructor import Plots_Constructor

if __name__ == '__main__':
    simulation_state = Simulation_State()

    simulation_state.run()
    simulation_state.save_data()

    plots_constructor = Plots_Constructor()
    plots_constructor.population_nutrients_plots()














