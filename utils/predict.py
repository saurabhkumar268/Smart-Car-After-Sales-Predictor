import pickle
import pandas as pd
import os

# load model
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "price_model.pkl")
model = pickle.load(open(model_path, "rb"))

def predict_price(car_age, km_driven, fuel_type, transmission):
    
    # input to dataframe
    data = {
        "car_age": [car_age],
        "km_driven": [km_driven],
        "fuel_type": [fuel_type],
        "transmission": [transmission]
    }

    df = pd.DataFrame(data)

    # convert categorical
    df = pd.get_dummies(df)

    # ensure same columns as training
    model_columns = model.feature_names_in_
    for col in model_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[model_columns]

    # prediction
    price = model.predict(df)[0]

    return int(price)