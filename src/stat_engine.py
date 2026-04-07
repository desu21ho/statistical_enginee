# src/stat_engine.py

from typing import List, Union
import math

Number = Union[int, float]


class StatEngine:
    def __init__(self, data: List[Number]):
        self.data = self._clean_data(data)

        if len(self.data) == 0:
            raise ValueError("Dataset is empty after cleaning.")

    def _clean_data(self, data):
        """Ensure all elements are numeric."""
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")

        cleaned = []
        for value in data:
            if isinstance(value, (int, float)):
                cleaned.append(float(value))
            else:
                raise TypeError(f"Invalid data type detected: {value}")

        return cleaned

    # ---------------------------
    # CENTRAL TENDENCY
    # ---------------------------

    def get_mean(self) -> float:
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def get_mode(self):
        frequency = {}

        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1

        max_freq = max(frequency.values())

        if max_freq == 1:
            return "No mode (all values are unique)"

        modes = [k for k, v in frequency.items() if v == max_freq]
        return modes

    # ---------------------------
    # DISPERSION
    # ---------------------------

    def get_variance(self, is_sample=True) -> float:
        n = len(self.data)
        mean = self.get_mean()

        if is_sample:
            if n < 2:
                raise ValueError("Sample variance requires at least 2 data points.")
            denominator = n - 1  # Bessel’s correction
        else:
            denominator = n

        variance = sum((x - mean) ** 2 for x in self.data) / denominator
        return variance

    def get_standard_deviation(self, is_sample=True) -> float:
        variance = self.get_variance(is_sample)
        return math.sqrt(variance)

    # ---------------------------
    # OUTLIER DETECTION
    # ---------------------------

    def get_outliers(self, threshold=2) -> List[float]:
        mean = self.get_mean()
        std = self.get_standard_deviation()

        if std == 0:
            return []

        outliers = [
            x for x in self.data
            if abs(x - mean) > threshold * std
        ]

        return outliers
