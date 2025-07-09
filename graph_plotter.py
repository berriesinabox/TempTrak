import matplotlib.pyplot as plt
import csv
from datetime import datetime

# File path
file_path = "data/weather_log.csv"

# Data lists
timestamps = []
temperatures = []
humidities = []

# Read the CSV file
with open(file_path, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        timestamps.append(datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S"))
        temperatures.append(int(row["Temperature"]))
        humidities.append(int(row["Humidity"]))

# Show only last 15 readings
timestamps = timestamps[-15:]
temperatures = temperatures[-15:]
humidities = humidities[-15:]

# Plot Temperature and Humidity
plt.figure(figsize=(10, 5))
plt.plot(timestamps, temperatures, label="Temperature (°C)", color='tomato', marker='o')
plt.plot(timestamps, humidities, label="Humidity (%)", color='skyblue', marker='x')

plt.title("🌡️ TempTrak: Last 15 Weather Readings")
plt.xlabel("Timestamp")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph as an image
plt.savefig("data/graph.png")

# Show the graph
plt.show()
