# Import libraries
import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer
# Create feature
feature = np.array([["Texas"],
                    ["California"],
                    ["Texas"],
                    ["Delaware"],
                    ["Texas"]])
# Create one-hot encoder
one_hot = LabelBinarizer()
# One-hot encode feature
one_hot.fit_transform(feature)
