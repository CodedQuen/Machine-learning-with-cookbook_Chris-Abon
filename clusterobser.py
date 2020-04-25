# Load libraries
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
# Make simulated feature matrix
features, _ = make_blobs(n_samples = 50,
                         n_features = 2,
                         centers = 3,
                         random_state = 1)
# Create DataFrame
dataframe = pd.DataFrame(features, columns=["feature_1", "feature_2"])
# Make k-means clusterer
clusterer = KMeans(3, random_state=0)
# Fit clusterer
clusterer.fit(features)
# Predict values
dataframe["group"] = clusterer.predict(features)
# View first few observations
dataframe.head(5)
