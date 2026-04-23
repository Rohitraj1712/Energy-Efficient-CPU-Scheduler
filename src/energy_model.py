def calculate_energy(burst_time, frequency):
    """
    Energy model:
    Energy ∝ Frequency^2 × Time
    """
    k = 1  # constant (can be adjusted)
    energy = k * (frequency ** 2) * burst_time
    return energy


def assign_frequency(burst_time):
    """
    Simple DVFS logic:
    - Small tasks → low frequency
    - Large tasks → high frequency
    """
    if burst_time <= 4:
        return 1.0   # low frequency
    else:
        return 2.0   # high frequency