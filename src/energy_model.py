def calculate_energy(burst_time, frequency):
    """
    Energy model:
    Energy ∝ Frequency^2 × Time
    """
    k = 1
    return k * (frequency ** 2) * burst_time


def assign_frequency(burst_time):
    """
    Basic DVFS logic (Day 4)
    """
    if burst_time <= 4:
        return 1.0
    else:
        return 2.0


def predict_burst(previous_burst, current_burst):
    """
    Workload prediction using averaging
    """
    return (previous_burst + current_burst) / 2


def dynamic_frequency(predicted_burst):
    """
    DVFS based on predicted workload
    """
    if predicted_burst <= 4:
        return 1.0
    elif predicted_burst <= 7:
        return 1.5
    else:
        return 2.0