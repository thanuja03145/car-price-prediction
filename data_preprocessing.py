import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

class DataPreprocessor:
    def __init__(self):
        self.categorical_features = ['fuel_type', 'transmission']
        self.numerical_features = ['year', 'mileage', 'engine_size']
        
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), self.numerical_features),
                ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), self.categorical_features)
            ]
        )

    def fit_transform(self, df):
        X = df[self.numerical_features + self.categorical_features]
        y = df['price'].values
        
        X_processed = self.preprocessor.fit_transform(X)
        
        # Get feature names after one-hot encoding
        cat_encoder = self.preprocessor.named_transformers_['cat']
        encoded_cat_features = cat_encoder.get_feature_names_out(self.categorical_features)
        feature_names = self.numerical_features + list(encoded_cat_features)
        
        return X_processed, y, feature_names

    def transform(self, df):
        X = df[self.numerical_features + self.categorical_features]
        return self.preprocessor.transform(X)
