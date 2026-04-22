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