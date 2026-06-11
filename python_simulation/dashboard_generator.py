import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime
import os

os.makedirs("images", exist_ok=True)
os.makedirs("data", exist_ok=True)

def generate_dashboard(data):

    timestamp = datetime.now()

    if data["aqi"] <= 50:
        status = "Good"
    elif data["aqi"] <= 100:
        status = "Moderate"
    elif data["aqi"] <= 200:
        status = "Poor"
    else:
        status = "Hazardous"

    row = {
        "Timestamp": timestamp,
        "AQI": data["aqi"],
        "Temperature": data["temperature"],
        "Humidity": data["humidity"],
        "Status": status
    }

    try:
        df = pd.read_csv("data/air_quality_logs.csv")
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    except:
        df = pd.DataFrame([row])

    df.to_csv("data/air_quality_logs.csv", index=False)

    history = pd.DataFrame({
        "AQI": [random.randint(40, 250) for _ in range(30)],
        "Temperature": [random.randint(20, 40) for _ in range(30)],
        "Humidity": [random.randint(35, 85) for _ in range(30)]
    })

    # Dashboard Pie Chart
    labels = ["Good", "Moderate", "Poor", "Hazardous"]
    values = [40, 25, 20, 15]

    plt.figure(figsize=(7, 5))
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Air Quality Dashboard Summary")
    plt.savefig("images/dashboard.png")
    plt.close()

    # Sensor Readings
    plt.figure(figsize=(8, 5))

    sensors = ["AQI", "Temperature", "Humidity"]
    values = [
        data["aqi"],
        data["temperature"],
        data["humidity"]
    ]

    bars = plt.bar(sensors, values)

    plt.title("Current Sensor Readings")
    plt.ylabel("Value")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.1f}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()
    plt.savefig("images/sensor_readings.png")
    plt.close()

    # Trend Analysis
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    axs[0].plot(history["AQI"])
    axs[0].set_title("AQI Trend")

    axs[1].plot(history["Temperature"])
    axs[1].set_title("Temperature Trend")

    axs[2].plot(history["Humidity"])
    axs[2].set_title("Humidity Trend")

    plt.tight_layout()
    plt.savefig("images/output_graphs.png")
    plt.close()

    # AQI Comparison
    categories = ["Good", "Moderate", "Poor", "Hazardous"]
    values = [50, 100, 200, 300]

    plt.figure(figsize=(8, 5))

    bars = plt.bar(categories, values)

    plt.title("AQI Classification Levels")
    plt.ylabel("AQI Value")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha="center",
            va="bottom"
        )

    plt.tight_layout()
    plt.savefig("images/aqi_comparison.png")
    plt.close()

    print("\nGenerated Images:")
    print("dashboard.png")
    print("sensor_readings.png")
    print("output_graphs.png")
    print("aqi_comparison.png")