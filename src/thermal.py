def thermal_scheduler(processes):
    """
    Simulate thermal-aware scheduling
    """
    core_temp = [30, 30]  # two cores with initial temperature
    threshold = 50

    allocation = []

    for p in processes:
        # choose cooler core
        if core_temp[0] <= core_temp[1]:
            core = 0
        else:
            core = 1

        # if chosen core is too hot, switch
        if core_temp[core] > threshold:
            core = 1 - core

        core_temp[core] += p['burst'] * 2  # increase temp based on workload

        allocation.append({
            'Process': p['id'],
            'Core': core,
            'Temperature': core_temp[core]
        })

    return allocation