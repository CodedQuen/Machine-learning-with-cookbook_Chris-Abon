# Load libraries
import numpy as np
from fancyimpute import KNN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs
# Make a simulated feature matrix
features, _ = make_blobs(n_samples = 1000,
                         n_features = 2,
                         random_state = 1)
# Standardize the features
scaler = StandardScaler()
standardized_features = scaler.fit_transform(features)
# Replace the first feature's first value with a missing value
true_value = standardized_features[0,0]
standardized_features[0,0] = np.nan
# Predict the missing values in the feature matrix
features_knn_imputed = KNN(k=5, verbose=0).complete(standardized_features)
# Compare true and imputed values
print("True Value:", true_value)
print("Imputed Value:", features_knn_imputed[0,0])
