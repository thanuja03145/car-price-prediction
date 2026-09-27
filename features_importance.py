import numpy as np

class FeatureExplainer:
    def __init__(self, feature_names=None):
        self.feature_names = feature_names if feature_names is not None else []

    def get_importance_scores(self, input_vector):
        # Generates basic feature importance visualization weights
        importance = np.abs(input_vector[0])
        total = np.sum(importance) + 1e-8
        normalized_scores = (importance / total) * 100
        
        # Fallback feature names if not provided
        if not self.feature_names:
            names = [f"Feature_{i}" for i in range(len(normalized_scores))]
        else:
            names = self.feature_names

        feature_dict = dict(zip(names, normalized_scores))
        sorted_features = sorted(feature_dict.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_features[:5])  # Top 5 features
