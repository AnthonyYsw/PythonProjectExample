# main.py only saves the main function and imports other modules.

import data_processing
import visualisation

from config import config_data

from pprint import pprint

def main():
    # .toml configuration loading
    pprint(config_data, sort_dicts=False)

    # Load data
    data = data_processing.load_data("data/dataset_1.csv")
    
    # Plot and save data
    visualisation.plot_data(data)

if __name__ == "__main__":
    main()
