# Load library
import numpy as np
# Create feature matrix
features = np.array([[1.1, 11.1],
                     [2.2, 22.2],
                     [3.3, 33.3],
                     [4.4, 44.4],
                     [np.nan, 55]])
# Keep only observations that are not (denoted by ~) missing
features[~np.isnan(features).any(axis=1)]
