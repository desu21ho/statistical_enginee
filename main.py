# main.py

from src.stat_engine import StatEngine
from src.monte_carlo import run_experiment


def main():
    data = [10, 20, 20, 30, 40, 100]

    engine = StatEngine(data)

    print("Mean:", engine.get_mean())
    print("Median:", engine.get_median())
    print("Mode:", engine.get_mode())
    print("Variance:", engine.get_variance())
    print("Standard Deviation:", engine.get_standard_deviation())
    print("Outliers:", engine.get_outliers())

    print("\n--- Monte Carlo Simulation ---")
    run_experiment()


if __name__ == "__main__":
    main()
