import random

def generate_sensor_data():
    return {
        "aqi": random.randint(20, 300),
        "temperature": round(random.uniform(18, 40), 2),
        "humidity": round(random.uniform(30, 90), 2)
    }