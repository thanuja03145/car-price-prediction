import os
import torch
import pandas as pd
import numpy as np
import joblib
from ml.data_preprocessing import DataPreprocessor
from ml.dnn_model import CarPriceDNN

def train():
    os.makedirs('models', exist_ok=True)
    os.makedirs('data', exist_ok=True)

    # Dummy Dataset Creation
    data = {
        'year': np.random.randint(2015, 2024, 500),
        'mileage': np.random.randint(10000, 150000, 500),
        'engine_size': np.random.uniform(1.0, 3.5, 500),
        'fuel_type': np.random.choice(['Petrol', 'Diesel', 'CNG'], 500),
        'transmission': np.random.choice(['Manual', 'Automatic'], 500),
        'price': np.random.randint(300000, 2500000, 500)
    }
    df = pd.DataFrame(data)
    df.to_csv('data/used_cars.csv', index=False)

    # Preprocessing
    preprocessor = DataPreprocessor()
    X_processed, y, feature_names = preprocessor.fit_transform(df)

    # Train PyTorch Model
    input_dim = X_processed.shape[1]
    model = CarPriceDNN(input_dim)
    
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    X_tensor = torch.tensor(X_processed, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.float32).view(-1, 1)

    model.train()
    for epoch in range(100):
        optimizer.zero_grad()
        outputs = model(X_tensor)
        loss = criterion(outputs, y_tensor)
        loss.backward()
        optimizer.step()

    # Save artifacts
    torch.save(model.state_dict(), 'models/dnn_model.pth')
    joblib.dump(preprocessor, 'models/preprocessor.pkl')
    joblib.dump(feature_names, 'models/feature_names.pkl')
    print("Model and Preprocessor saved successfully in 'models/' folder!")

if __name__ == '__main__':
    train()
