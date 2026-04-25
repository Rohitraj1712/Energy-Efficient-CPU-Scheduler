import matplotlib.pyplot as plt

def plot_comparison(fcfs_avg, rr_avg, energy_avg):
    algorithms = ['FCFS', 'Round Robin', 'Energy Efficient']
    values = [fcfs_avg, rr_avg, energy_avg]

    plt.bar(algorithms, values)
    plt.title("Performance vs Energy Trade-off")
    plt.xlabel("Algorithms")
    plt.ylabel("Waiting Time")
    plt.savefig("results/waiting_time.png")
    plt.show()
    plt.grid(True)


def plot_energy(energy_values):
    processes = [f"P{i+1}" for i in range(len(energy_values))]

    plt.plot(processes, energy_values, marker='o')
    plt.title("Energy Consumption per Process using DVFS")
    plt.xlabel("Processes")
    plt.ylabel("Energy")
    plt.savefig("results/energy.png")
    plt.show()
    plt.grid(True)