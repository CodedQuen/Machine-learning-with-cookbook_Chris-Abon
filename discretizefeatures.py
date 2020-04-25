# Load libraries
import numpy as np
from sklearn.preprocessing import Binarizer
# Create feature
age = np.array([[6],
                [12],
                [20],
                [36],
                [65]])
# Create binarizer
binarizer = Binarizer(18)
# Transform feature
binarizer.fit_transform(age)
