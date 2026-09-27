class MaintenanceEstimator:
    def __init__(self):
        pass

    def estimate_costs(self, age, mileage):
        # Base annual maintenance calculation
        base_cost = 500.0
        age_factor = age * 150.0
        mileage_factor = (mileage / 10000.0) * 100.0
        
        annual_cost = base_cost + age_factor + mileage_factor
        return round(annual_cost, 2)
