def fcfs_scheduling(processes):
    # Sort processes based on arrival time
    processes.sort(key=lambda x: x['arrival'])

    current_time = 0
    results = []

    for p in processes:
        # If CPU is idle, jump to arrival time
        if current_time < p['arrival']:
            current_time = p['arrival']

        start_time = current_time
        finish_time = start_time + p['burst']

        waiting_time = start_time - p['arrival']
        turnaround_time = finish_time - p['arrival']

        results.append({
            'Process': p['id'],
            'Start': start_time,
            'Finish': finish_time,
            'Waiting': waiting_time,
            'Turnaround': turnaround_time
        })

        current_time = finish_time

    return results