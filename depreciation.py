class DepreciationCalculator:
    def __init__(self, annual_rate=0.15):
        self.rate = annual_rate

    def calculate_future_value(self, current_price, years=5):
        future_values = {}
        for y in range(1, years + 1):
            val = current_price * ((1 - self.rate) ** y)
            future_values[f"Year {y}"] = round(val, 2)
        return future_values
