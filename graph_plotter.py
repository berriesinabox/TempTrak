import matplotlib.pyplot as plt
import csv
from datetime import datetime


file_path = "data/weather_log.csv"


timestamps = []
temperatures = []
humidities = []


with open(file_path, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        timestamps.append(datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S"))
        temperatures.append(int(row["Temperature"]))
        humidities.append(int(row["Humidity"]))


timestamps = timestamps[-15:]
temperatures = temperatures[-15:]
humidities = humidities[-15:]


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
plt.savefig("data/graph.png")
plt.show()
