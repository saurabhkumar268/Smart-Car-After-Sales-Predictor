import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# load dataset
file_path = os.path.join(os.path.dirname(__file__), "..", "data", "easy_cars.csv")
df = pd.read_csv(file_path)

# convert categorical → numerical
df = pd.get_dummies(df, drop_first=True)

# features & target
X = df.drop("price", axis=1)
y = df["price"]

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# save model
model_path = os.path.join(os.path.dirname(__file__), "price_model.pkl")
pickle.dump(model, open(model_path, "wb"))

print("✅ Model trained & saved!")