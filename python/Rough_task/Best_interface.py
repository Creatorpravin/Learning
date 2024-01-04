def choose_best_interface(interface1_metrics, interface2_metrics, dynamic_thresholds, dynamic_thresholds2):
    """
    Choose the best interface based on changing threshold values for latency, jitter, and packet loss.

    Parameters:
    - interface1_metrics: Dictionary of metrics for interface 1 (e.g., {'latency': 25, 'jitter': 5, 'loss': 1}).
    - interface2_metrics: Dictionary of metrics for interface 2.
    - dynamic_thresholds: Dictionary of dynamic threshold values (e.g., {'latency': 30, 'jitter': 10, 'loss': 5}).

    Returns:
    - best_interface: String indicating the best interface ('interface1' or 'interface2').
    """
    performance_score = {'interface1': 3, 'interface2': 3}

    for metric in ['latency', 'jitter', 'loss']:
        # Compare for Interface 1
        if metric in interface1_metrics and metric in dynamic_thresholds:
            if interface1_metrics[metric] <= dynamic_thresholds[metric]:
                performance_score['interface1'] -= 1

        # Compare for Interface 2
        if metric in interface2_metrics and metric in dynamic_thresholds2:
            if interface2_metrics[metric] <= dynamic_thresholds2[metric]:
                performance_score['interface2'] -= 1
    print(performance_score)
    # Choose the interface with the higher performance score
    best_interface = min(performance_score, key=performance_score.get)

    return best_interface

# Example usage:
interface1_metrics = {'latency': 25, 'jitter': 5, 'loss': 5}
interface2_metrics = {'latency': 25, 'jitter': 5, 'loss': 1}
dynamic_thresholds = {'latency': 30, 'jitter': 10, 'loss': 5}
dynamic_thresholds2 = {'latency': 35, 'jitter': 15, 'loss': 2}

best_interface = choose_best_interface(interface1_metrics, interface2_metrics, dynamic_thresholds, dynamic_thresholds2)
print(f"The best interface is: {best_interface}")
