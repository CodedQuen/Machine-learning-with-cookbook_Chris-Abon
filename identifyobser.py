# Load libraries
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs
# Create simulated data
features, _ = make_blobs(n_samples = 10,
                         n_features = 2,
                         centers = 1,
                         random_state = 1)
# Replace the first observation's values with extreme values
features[0,0] = 10000
features[0,1] = 10000
outlier_detector = EllipticEnvelope(contamination=.1)
# Fit detector
outlier_detector.fit(features)
# Predict outliers
outlier_detector.predict(features)
