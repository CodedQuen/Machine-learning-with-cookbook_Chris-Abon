# Import library
from sklearn.feature_extraction import DictVectorizer
# Create dictionary
data_dict = [{"Red": 2, "Blue": 4},
             {"Red": 4, "Blue": 3},
             {"Red": 1, "Yellow": 2},
             {"Red": 2, "Yellow": 2}]

dictvectorizer = DictVectorizer(sparse=False)
# Convert dictionary to feature matrix
features = dictvectorizer.fit_transform(data_dict)
# View feature matrix
features
