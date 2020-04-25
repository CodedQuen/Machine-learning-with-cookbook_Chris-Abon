# Load libraries
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
# Create feature matrix
features = np.array([[2, 3],
                     [2, 3],
                     [2, 3]])
# Create PolynomialFeatures object
polynomial_interaction = PolynomialFeatures(degree=2, include_bias=False)
# Create polynomial features
polynomial_interaction.fit_transform(features)
