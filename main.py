from src.fcfs import fcfs_scheduling

# Sample processes
processes = [
    {'id': 'P1', 'arrival': 0, 'burst': 5},
    {'id': 'P2', 'arrival': 1, 'burst': 3},
    {'id': 'P3', 'arrival': 2, 'burst': 8},
]

result = fcfs_scheduling(processes)

print("\nFCFS Scheduling Result:\n")
for r in result:
    print(r)
    from src.round_robin import round_robin_scheduling

print("\nRound Robin Scheduling Result:\n")

rr_result = round_robin_scheduling(processes, time_quantum=2)

for r in rr_result:
    print(r)
    from src.energy_model import calculate_energy, assign_frequency

print("\nEnergy Calculation:\n")

for p in processes:
    freq = assign_frequency(p['burst'])
    energy = calculate_energy(p['burst'], freq)

    print(f"Process {p['id']} → Frequency: {freq}, Energy: {energy}")
    from src.energy_model import predict_burst, dynamic_frequency, calculate_energy

print("\nDVFS + Workload Prediction:\n")

previous_burst = 5  # initial assumption

for p in processes:
    predicted = predict_burst(previous_burst, p['burst'])
    freq = dynamic_frequency(predicted)
    energy = calculate_energy(p['burst'], freq)

    print(f"Process {p['id']} → Predicted: {predicted}, Frequency: {freq}, Energy: {energy}")

    previous_burst = p['burst']
    from src.thermal import thermal_scheduler

print("\nThermal-Aware Scheduling:\n")

thermal_result = thermal_scheduler(processes)

for t in thermal_result:
    print(t)
    from src.visualization import plot_comparison, plot_energy

# Example values (you can calculate properly later)
fcfs_avg = sum([r['Waiting'] for r in result]) / len(result)
rr_avg = sum([r['Waiting'] for r in rr_result]) / len(rr_result)

energy_values = []
previous_burst = 5

for p in processes:
    predicted = predict_burst(previous_burst, p['burst'])
    freq = dynamic_frequency(predicted)
    energy = calculate_energy(p['burst'], freq)

    energy_values.append(energy)
    previous_burst = p['burst']

energy_avg = sum(energy_values) / len(energy_values)

plot_comparison(fcfs_avg, rr_avg, energy_avg)
plot_energy(energy_values)

print("\nNote: Energy-efficient scheduling trades slight performance for reduced energy.\n")