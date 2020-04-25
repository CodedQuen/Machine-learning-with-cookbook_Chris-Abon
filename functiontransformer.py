# Load libraries
import numpy as np
from sklearn.preprocessing import FunctionTransformer
# Create feature matrix
features = np.array([[2, 3],
                     [2, 3],
                     [2, 3]])
# Define a simple function
def add_ten(x):
    return x + 10
# Create transformer
ten_transformer = FunctionTransformer(add_ten)
# Transform feature matrix
ten_transformer.transform(features)
