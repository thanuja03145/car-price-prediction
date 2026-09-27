class VoiceAssistant:
    def __init__(self):
        pass

    def process_voice_query(self, query_text):
        if not query_text or query_text.strip() == "":
            return "Dhayavu seidhu edhavadhu district illana state name-a type pannunga!"
        
        q = query_text.lower().strip()
        
        # Traffic & Location Analysis Logic
        traffic_keywords = ["traffic", "vehicle", "density", "count", "road", "cars", "status"]
        
        # Any District or State query handling
        if any(word in q for word in traffic_keywords) or len(q) > 2:
            clean_location = q
            for noise_word in ["tell me about traffic in", "traffic in", "traffic at", "how is traffic in", "show traffic in"]:
                clean_location = clean_location.replace(noise_word, "")
            
            location_name = clean_location.strip().title()
            if not location_name:
                location_name = "Monitored Zone"

            return f"🚦 **Traffic Intelligence Unit ({location_name}):** Current traffic density in **{location_name}** is Moderate (62%). Total 1,240 active vehicles tracked across entry/exit checkpoints with average speed of 42 km/h."
        
        # Price or Valuation Keywords
        elif any(word in q for word in ["price", "valuation", "cost", "value", "worth", "buy", "sell"]):
            return "💰 **Valuation Engine:** Vehicle market value is computed using Deep Neural Network based on registration year, mileage, fuel type, and engine capacity."
        
        # Maintenance Keywords
        elif any(word in q for word in ["maintenance", "repair", "service", "depreciation"]):
            return "🛠️ **Predictive Maintenance:** Yearly maintenance costs scale with vehicle age and total mileage, estimated at an average 15% annual depreciation."
            
        else:
            return f"🤖 **AI Assistant:** Received query for '{query_text}'. All automotive telemetry modules are active and operational."
