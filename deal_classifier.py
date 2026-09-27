class DealClassifier:
    @staticmethod
    def classify(predicted_price, listing_price):
        diff_percentage = ((listing_price - predicted_price) / predicted_price) * 100
        
        if diff_percentage <= -8:
            return "Great Deal 🔥", "Success"
        elif -8 < diff_percentage <= 5:
            return "Fair Price 👍", "Info"
        else:
            return "Overpriced ⚠️", "Warning"
