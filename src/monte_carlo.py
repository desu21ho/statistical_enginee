# src/monte_carlo.py

import random


def simulate_crashes(days: int) -> float:
    """Simulate server crashes over given days."""
    crash_probability = 0.045
    crashes = 0

    for _ in range(days):
        if random.random() < crash_probability:
            crashes += 1

    return crashes / days


def run_experiment():
    test_days = [10, 100, 1000]

    for days in test_days:
        simulated_prob = simulate_crashes(days)
        print(f"Days: {days}, Simulated Crash Probability: {simulated_prob:.4f}")
