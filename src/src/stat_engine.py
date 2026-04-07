import math
class StatEngine:
    def __init__(self, data):
        if not data:
            raise ValueError("Empty data")
        for x in data:
            if not isinstance(x, (int, float)):
                raise TypeError("Only numbers allowed")
        self.data = data

    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        d = sorted(self.data)
        n = len(d)
        mid = n // 2

        if n % 2 == 0:
            return (d[mid-1] + d[mid]) / 2
        return d[mid]

    def get_mode(self):
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1
        max_f = max(freq.values())

        if max_f == 1:
            return "No mode"

        return [k for k, v in freq.items() if v == max_f]

    def get_variance(self, is_sample=True):
        mean = self.get_mean()
        n = len(self.data)
        denom = n-1 if is_sample else n
        return sum((x - mean) ** 2 for x in self.data) / denom

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        return [x for x in self.data if abs(x - mean) > threshold * std]
