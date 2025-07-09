import random
import time

def get_weather():
    temp = random.randint(20, 35)
    humidity = random.randint(40, 70)
    return temp, humidity

print("🌤️ Starting weather simulator...\n")

while True:
    temp, humidity = get_weather()
    print(f"Temperature: {temp}°C | Humidity: {humidity}%")
    time.sleep(2)  # wait for 2 seconds before showing next reading
