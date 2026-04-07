#  Statistical Engineering & Simulation Engine

##  Project Overview

This project implements a pure Python statistical engine from scratch without using external libraries. It processes raw numerical data and provides key statistical measures including mean, median, mode, variance, standard deviation, and outlier detection.

In addition, the project includes a Monte Carlo simulation to model a server crash scenario and demonstrate the Law of Large Numbers (LLN).

---

##  Mathematical Logic

### Mean

The mean is calculated as:
Mean = Sum of all values / Number of values

---

### Median

* If the dataset size is **odd** → the middle value after sorting is returned
* If the dataset size is **even** → the average of the two middle values is returned

---

### Variance

Variance measures how far data points are spread from the mean.

* **Population Variance**:
  Variance = Σ(x - μ)² / N

* **Sample Variance (Bessel’s Correction)**:
  Variance = Σ(x - x̄)² / (N - 1)

---

### Standard Deviation

Standard deviation is the square root of variance and represents data dispersion.

---

### Outliers

Outliers are detected as values that are more than a specified number of standard deviations away from the mean.

---

##  Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/statistical_engine.git
```

2. Navigate into the project directory:

```bash
cd statistical_engine
```

3. Run the program:

```bash
python main.py
```

---

##  Testing

Run the unit tests using the following command:

```bash
python -m unittest discover tests
```

---

##  Law of Large Numbers (LLN)

The Law of Large Numbers states that as the number of trials increases, the experimental probability approaches the theoretical probability.

In this project:

* Small simulations (e.g., 30 days) produce unstable results
* Larger simulations (e.g., 10,000 days) converge closer to the true probability (0.045)

---
