import json
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

with open("data/sample_salaries.json") as f:
    data = json.load(f)

s = StatEngine(data)

print("Mean:", s.get_mean())
print("Median:", s.get_median())
print("Mode:", s.get_mode())
print("Std:", s.get_standard_deviation())
print("Outliers:", s.get_outliers())

for d in [30, 365, 10000]:
    c, p = simulate_crashes(d)
    print(d, "days →", p)
