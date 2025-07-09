import random
import time
import os

if not os.path.exists("data"):
    os.makedirs("data")

log_file = "data/weather_log.csv"

if not os.path.exists(log_file) or os.stat(log_file).st_size == 0:
    with open(log_file, "w") as f:
        f.write("Temperature(°C),Humidity(%),Timestamp\n")

def get_weather():
    temp = random.randint(20, 35)
    humidity = random.randint(40, 70)
    return temp, humidity

print("🌡️ TempTrak v2 Logging Started...\n")

while True:
    temp, humidity = get_weather()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    if temp > 32:
        status = "Hot"
    elif temp < 24:
        status = "Cool"
    else:
        status = "Normal"

    print(f"🌤️ Temp: {temp}°C |💧 Humidity: {humidity}% | 🕒 {timestamp} | Status: {status}")

    with open(log_file, "a") as f:
        f.write("Temperature,Humidity,Timestamp,Status\n")

    time.sleep(2)
