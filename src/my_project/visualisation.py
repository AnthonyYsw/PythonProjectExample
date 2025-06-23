import matplotlib.pyplot as plt
from config import grandparent_dir

def plot_data(data):
    # Extract current and voltage
    current = data[:, 0]
    voltage = data[:, 1]
    
    # Plot the data
    plt.figure(figsize=(8, 5))
    plt.plot(current, voltage, marker='o', linestyle='-')
    plt.title("Current vs Voltage")
    plt.xlabel("Current (I)")
    plt.ylabel("Voltage (V)")
    plt.grid(True)
    plt.savefig(f"{grandparent_dir}/imgs/plot_current_vs_voltage.png")
    plt.show()
