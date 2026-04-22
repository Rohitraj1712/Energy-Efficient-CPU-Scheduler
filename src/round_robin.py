def round_robin_scheduling(processes, time_quantum):
    queue = []
    time = 0
    results = []
    
    # Copy processes and initialize remaining burst time
    for p in processes:
        p['remaining'] = p['burst']

    processes.sort(key=lambda x: x['arrival'])
    n = len(processes)
    i = 0

    while i < n or queue:
        # Add arrived processes to queue
        while i < n and processes[i]['arrival'] <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time = processes[i]['arrival']
            continue

        current = queue.pop(0)

        start_time = time
        exec_time = min(time_quantum, current['remaining'])
        time += exec_time
        current['remaining'] -= exec_time

        # Add new processes arrived during execution
        while i < n and processes[i]['arrival'] <= time:
            queue.append(processes[i])
            i += 1

        if current['remaining'] > 0:
            queue.append(current)
        else:
            finish_time = time
            waiting_time = finish_time - current['arrival'] - current['burst']
            turnaround_time = finish_time - current['arrival']

            results.append({
                'Process': current['id'],
                'Finish': finish_time,
                'Waiting': waiting_time,
                'Turnaround': turnaround_time
            })

    return results