import streamlit as st
import matplotlib.pyplot as plt

from src.fcfs import fcfs_scheduling
from src.round_robin import round_robin_scheduling
from src.energy_model import predict_burst, dynamic_frequency, calculate_energy
from src.thermal import thermal_scheduler

# Page config
st.set_page_config(page_title="CPU Scheduler", layout="wide")

# Sidebar
st.sidebar.title("⚙️ Controls")

st.title("⚡ Energy Efficient CPU Scheduling")
st.markdown("### Interactive Simulation")

# Input
st.sidebar.header("🔧 Input Processes")

n = st.sidebar.number_input("Number of Processes", min_value=1, max_value=5, value=3)

default_arrivals = [0, 1, 2]
default_bursts = [5, 3, 8]

processes = []

for i in range(n):
    st.sidebar.subheader(f"Process P{i+1}")

    arrival = st.sidebar.number_input(
        f"Arrival Time P{i+1}",
        value=default_arrivals[i] if i < len(default_arrivals) else 0,
        key=f"a{i}"
    )

    burst = st.sidebar.number_input(
        f"Burst Time P{i+1}",
        value=default_bursts[i] if i < len(default_bursts) else 1,
        key=f"b{i}"
    )

    processes.append({'id': f'P{i+1}', 'arrival': arrival, 'burst': burst})

quantum = st.sidebar.number_input("Time Quantum (RR)", value=2)

# Run Simulation
if st.button("🚀 Run Simulation"):

    # FCFS
    fcfs_result = fcfs_scheduling(processes)
    st.subheader("📌 FCFS Result")
    st.write(fcfs_result)
    st.info("FCFS executes processes in order of arrival.")

    # Round Robin
    rr_result = round_robin_scheduling(processes, quantum)
    st.subheader("📌 Round Robin Result")
    st.write(rr_result)
    st.info("Round Robin ensures fairness using time slicing.")

    # Energy Efficient
    st.subheader("⚡ Energy Efficient Scheduling")

    previous_burst = 5
    energy_results = []

    for p in processes:
        predicted = predict_burst(previous_burst, p['burst'])
        freq = dynamic_frequency(predicted)
        energy = calculate_energy(p['burst'], freq)

        energy_results.append({
            "Process": p['id'],
            "Predicted": predicted,
            "Frequency": freq,
            "Energy": energy
        })

        previous_burst = p['burst']

    st.write(energy_results)
    st.info("DVFS dynamically adjusts CPU frequency to reduce energy consumption.")

    # Thermal
    st.subheader("🌡 Thermal Scheduling")
    thermal_result = thermal_scheduler(processes)
    st.write(thermal_result)
    st.info("Thermal scheduling distributes load to prevent overheating.")

    # Summary
    st.subheader("📊 Summary")

    fcfs_avg = sum([r['Waiting'] for r in fcfs_result]) / len(fcfs_result)
    rr_avg = sum([r['Waiting'] for r in rr_result]) / len(rr_result)
    energy_avg = sum([e['Energy'] for e in energy_results]) / len(energy_results)

    st.write(f"FCFS Avg Waiting Time: {fcfs_avg}")
    st.write(f"Round Robin Avg Waiting Time: {rr_avg}")
    st.write(f"Average Energy Consumption: {energy_avg}")

    # Graphs
    st.subheader("📈 Graphical Analysis")

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(5, 3))
        algorithms = ['FCFS', 'Round Robin', 'Energy Efficient']
        values = [fcfs_avg, rr_avg, energy_avg]

        ax1.bar(algorithms, values)
        ax1.set_title("Performance vs Energy")
        ax1.grid(True)

        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        names = [e['Process'] for e in energy_results]
        energies = [e['Energy'] for e in energy_results]

        ax2.plot(names, energies, marker='o')
        ax2.set_title("Energy (DVFS)")
        ax2.grid(True)

        st.pyplot(fig2)

    st.success("✔ Energy-efficient scheduling reduces energy with slight performance trade-off.")

# Footer
st.markdown("---")
st.markdown("Made for CSE316 Project 🚀")