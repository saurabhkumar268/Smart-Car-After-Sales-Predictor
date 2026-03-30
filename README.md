# 🚗 Smart Car After-Sales Predictor

## 📌 Overview

Smart Car After-Sales Predictor is a terminal-based machine learning project that helps users estimate a car’s resale value and analyze post-purchase insights such as maintenance cost, depreciation trends, and smart recommendations.

It provides a structured and intelligent system for better decision-making in buying or selling used cars.

------------------------------------------------------------------------

## 🚀 Features

- Resale Price Prediction using Machine Learning (Random Forest)
- Maintenance Cost Estimation (rule-based logic)
- Depreciation Trend Analysis (year-wise value drop)
- Smart Suggestions (sell/hold & maintenance alerts)
- Car Comparison (Car A vs Car B)
- Prediction History (stored in CSV)
- Interactive CLI-based menu system

------------------------------------------------------------------------

## ⚙️ How It Works

1. User enters car details:
   - Car Age
   - KM Driven
   - Fuel Type
   - Transmission

2. System processes input:
   - Predicts resale price using ML model
   - Estimates maintenance cost using logic

3. Additional insights provided:
   - Depreciation trend
   - Smart suggestions
   - Car score
   - Comparison (optional)

------------------------------------------------------------------------

## 🧠 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn (Random Forest Regressor)
- CSV (for data storage)
- Modular Programming (separate files for preprocessing, prediction, training)

------------------------------------------------------------------------

## 📂 Project Structure

car_predictor/

main.py

data/
- cars.csv
- easy_cars.csv

models/
- train_model.py
- price_model.pkl

utils/
- preprocess.py
- predict.py

history.csv

README.md

------------------------------------------------------------------------

## 🤖 Machine Learning

A Random Forest Regressor is used for predicting car resale prices.

Model is trained using features like:
- Car Age
- KM Driven
- Fuel Type
- Transmission

Categorical data is converted using encoding techniques before training.

------------------------------------------------------------------------

## ▶️ How to Run

1. Install required libraries:
   pip install pandas numpy scikit-learn

2. Train the model:
   python models/train_model.py

3. Run the project:
   python main.py

------------------------------------------------------------------------

## 📊 Example Output

Enter Car Details:
Age: 5
KM Driven: 40000
Fuel: Petrol
Transmission: Manual

Predicted Price: ₹450000
Maintenance: ₹12000/year

Depreciation Trend:
After 1 year: ₹405000
After 2 year: ₹364500

Suggestion:
Car is old, consider selling soon

Car Score: 8/10

------------------------------------------------------------------------

## 💡 Conclusion

This project transforms basic machine learning into a practical tool by combining prediction with real-world insights. It helps users make smarter after-sales decisions using data-driven analysis.

------------------------------------------------------------------------

## 🔮 Future Improvements

- Web-based UI using Streamlit
- Integration with real-time car datasets
- Advanced ML models for better accuracy
- Mobile app version
