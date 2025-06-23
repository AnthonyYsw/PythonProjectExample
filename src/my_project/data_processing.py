import numpy as np

def load_data(filepath):
    # Load data from a CSV file
    data = np.genfromtxt(filepath, delimiter=',', skip_header=1)
    return data

