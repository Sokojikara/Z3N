# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# dataset = pd.DataFrame({
#     "independent_variable": np.random.randint(100, 200, size=1000),
#     "dependent_variable": np.random.randint(50, 150, size=1000)
# })

# # Split the dataset into input (X) and output (y) variables
# X = dataset["independent_variable"]
# y = dataset["dependent_variable"]

# # Create a linear regression model
# model = LinearRegression()

# # Train the model
# model.fit(X.values.reshape(-1, 1), y.values.reshape(-1, 1))

# # Make predictions
# y_pred = model.predict(X.values.reshape(-1, 1))

# # Evaluate the model
# print("Model score: ", model.score(X.values.reshape(-1, 1), y.values.reshape(-1, 1)))

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("usa_housing_dataset.csv")

# Check the dataset
print(df.shape)
print(df.isnull().sum())

# Split the dataset into input (X) and output (y) variables
X = df[["Avg. Area Income", "Avg. Area House Age", "Avg. Area Number of Rooms",
               "Avg. Area Number of Bedrooms", "Area Population"]]
y = df["Price"]

# Split the dataset into training and test datasets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training dataset
model.fit(X_train, y_train)

# Make predictions on the test dataset
y_pred = model.predict(X_test)

# Evaluate the model
print("Model Score: ", model.score(X_test, y_test))

