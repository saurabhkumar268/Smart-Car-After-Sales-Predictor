from utils.predict import predict_price
import csv
import os

last_data = None  # store last prediction

# maintenance calculation
def calculate_maintenance(car_age, km):
    return int(2000 + (car_age * 1000) + (km / 10))

# depreciation
def show_depreciation(price, years=5):
    print("\n📉 Depreciation Trend:")
    temp_price = price
    for i in range(1, years + 1):
        temp_price *= 0.9
        print(f"After {i} year(s): ₹{int(temp_price)}")

# ✅ FIXED suggestions (always prints)
def get_suggestion(car_age, maintenance):
    print("\n💡 Smart Suggestions:")

    if car_age > 5:
        print("👉 Car is old, consider selling soon")
    else:
        print("👉 Car age is fine")

    if maintenance > 15000:
        print("⚠️ Maintenance is high")
    else:
        print("✅ Maintenance cost is normal")

# score
def car_score(price, maintenance, car_age):
    score = 10
    if maintenance > 15000:
        score -= 3
    if car_age > 5:
        score -= 2
    return max(score, 1)

# save history
def save_history(data):
    file_exists = os.path.isfile("history.csv")
    with open("history.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Age", "KM", "Fuel", "Transmission", "Price", "Maintenance"])
        writer.writerow(data)

# view history
def view_history():
    if not os.path.exists("history.csv"):
        print("No history found.")
        return
    with open("history.csv", "r") as file:
        print("\n📜 Prediction History:")
        print(file.read())

# ================= MAIN MENU =================
while True:
    print("\n===== 🚗 Smart Car Predictor =====")
    print("1. Predict Car Value & Maintenance")
    print("2. Show Depreciation Trend")
    print("3. Get Smart Suggestions")
    print("4. Car Score")
    print("5. Compare Cars")
    print("6. View History")
    print("7. Exit")

    choice = input("Enter choice: ")

    # 1️⃣ Prediction
    if choice == "1":
        age = int(input("Enter Car Age: "))
        km = int(input("Enter KM Driven: "))
        fuel = input("Fuel Type (Petrol/Diesel): ")
        trans = input("Transmission (Manual/Automatic): ")

        price = predict_price(age, km, fuel, trans)
        maintenance = calculate_maintenance(age, km)

        print(f"\n💰 Predicted Price: ₹{price}")
        print(f"🔧 Maintenance: ₹{maintenance}/year")

        # store data
        last_data = (age, km, fuel, trans, price, maintenance)

        # save history
        save_history(last_data)

    # 2️⃣ Depreciation
    elif choice == "2":
        if last_data:
            show_depreciation(last_data[4])
        else:
            print("⚠️ Pehle prediction karo")

    # 3️⃣ Suggestions ✅ FIXED
    elif choice == "3":
        if last_data:
            get_suggestion(last_data[0], last_data[5])
        else:
            print("⚠️ Pehle prediction karo")

    # 4️⃣ Score
    elif choice == "4":
        if last_data:
            score = car_score(last_data[4], last_data[5], last_data[0])
            print(f"⭐ Car Score: {score}/10")
        else:
            print("⚠️ Pehle prediction karo")

    # 5️⃣ Compare
    elif choice == "5":
        print("\n--- Car A ---")
        a_price = predict_price(
            int(input("Age: ")),
            int(input("KM: ")),
            input("Fuel: "),
            input("Transmission: ")
        )

        print("\n--- Car B ---")
        b_price = predict_price(
            int(input("Age: ")),
            int(input("KM: ")),
            input("Fuel: "),
            input("Transmission: ")
        )

        print("\n🔍 Comparison Result:")
        print("Better Price:", "Car A" if a_price > b_price else "Car B")

    # 6️⃣ History
    elif choice == "6":
        view_history()

    # 7️⃣ Exit
    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")