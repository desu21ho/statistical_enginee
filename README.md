# Statistical Engineering and Simulation assessment 

## Overview
This project implements a statistical analysis engine from scratch using Python standard libraries. It computes central tendency, dispersion, and detects outliers. It also includes a Monte Carlo simulation for server crash probability.

## Mathematical Logic

### Variance
Population Variance:
Var = Σ(x - μ)^2 / N

Sample Variance:
Var = Σ(x - x̄)^2 / (N - 1)

(Bessel’s correction is applied for sample variance)

### Median
- Odd: middle value
- Even: average of two middle values

## Setup Instructions

```bash
git clone <https://github.com/desu21ho/statistical_enginee.git>
cd statistical_enginee
python main.py
```
**Testing**
```
python -m unittest discover tests
```
**Acceptance Criteria**
 Handles empty list
 Handles invalid data types
 Supports multimodal distributions
 Correct sample vs population variance
 Outlier detection works
 Unit tests implemented
