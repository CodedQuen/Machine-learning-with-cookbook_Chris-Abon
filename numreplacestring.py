# Load library
import pandas as pd
# Create features
dataframe = pd.DataFrame({"Score": ["Low", "Low", "Medium", "Medium", "High"]})

# Create mapper
scale_mapper = {"Low":1,
                "Medium":2,
                "High":3}
# Replace feature values with scale
dataframe["Score"].replace(scale_mapper)
