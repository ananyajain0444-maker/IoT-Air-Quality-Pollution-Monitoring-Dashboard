from python_simulation.sensor_simulator import generate_sensor_data
from python_simulation.aqi_calculator import calculate_aqi
from python_simulation.alert_system import check_alert
from python_simulation.dashboard_generator import generate_dashboard

data = generate_sensor_data()

aqi_status = calculate_aqi(data["aqi"])
alert = check_alert(aqi_status)

print("\n===== AIR QUALITY REPORT =====")
print(f"AQI Value: {data['aqi']}")
print(f"Temperature: {data['temperature']} °C")
print(f"Humidity: {data['humidity']} %")
print(f"Status: {aqi_status}")
print(f"Alert: {alert}")

generate_dashboard(data)