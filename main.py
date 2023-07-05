from simulation_state.simulation_state import Simulation_State
from data_handler.data_handler import Data_Handler

if __name__ == '__main__':
    simulation_state = Simulation_State()

    simulation_state.run()
    simulation_state.end_simulation()
    simulation_state.save_data()

    data_handler = Data_Handler()
    data_handler.print_reds_data()












