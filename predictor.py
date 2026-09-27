import torch
import numpy as np

class PricePredictor:
    def __init__(self, model_path, preprocessor, input_dim):
        from ml.dnn_model import CarPriceDNN
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = CarPriceDNN(input_dim).to(self.device)
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.eval()
        self.preprocessor = preprocessor

    def predict(self, input_df):
        processed_data = self.preprocessor.transform(input_df)
        tensor_data = torch.tensor(processed_data, dtype=torch.float32).to(self.device)
        
        with torch.no_grad():
            prediction = self.model(tensor_data)
        
        return float(prediction.cpu().numpy()[0][0])
