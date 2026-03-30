import pandas as pd
import os

# path
file_path = os.path.join(os.path.dirname(__file__), "..", "data", "cars.csv")

# load
df = pd.read_csv(file_path)

# clean column names
df.columns = df.columns.str.strip().str.lower()

print("Columns in dataset:", df.columns)  # debug

# auto-detect columns
year_col = [col for col in df.columns if "year" in col][0]
price_col = [col for col in df.columns if "price" in col][0]
km_col = [col for col in df.columns if "km" in col][0]
fuel_col = [col for col in df.columns if "fuel" in col][0]
trans_col = [col for col in df.columns if "trans" in col][0]

# create clean dataset
df["car_age"] = 2024 - df[year_col]
df["km_driven"] = df[km_col]
df["fuel_type"] = df[fuel_col]
df["transmission"] = df[trans_col]
df["price"] = df[price_col]

easy_df = df[["car_age", "km_driven", "fuel_type", "transmission", "price"]]

# save
output_path = os.path.join(os.path.dirname(__file__), "..", "data", "easy_cars.csv")
easy_df.to_csv(output_path, index=False)

print("✅ Easy dataset created successfully!")