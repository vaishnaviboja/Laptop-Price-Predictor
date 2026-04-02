print("Program started")

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

data = {
    "RAM": [4, 8, 16],
    "Storage": [256, 512, 1024],
    "Price": [30000, 50000, 80000]
}

df = pd.DataFrame(data)

X = df[["RAM", "Storage"]]
y = df["Price"]

model = RandomForestRegressor()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully!")
