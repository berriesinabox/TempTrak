from tkinter import *
import random
import time
import csv
import os
import matplotlib.pyplot as plt
logging_job = None  # to store the loop ID



root = Tk()
root.title("🌡️ TempTrak - Weather Logger")
root.geometry("400x380")
root.configure(bg="#f0f0f0")
root.resizable(True, True)


# Heading Label
heading = Label(root, text="TempTrak", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#ff4d4d")
heading.pack(pady=10)

# Temperature Display
temp_label = Label(root, text="Temperature: --°C", font=("Arial", 14), bg="#f0f0f0")
temp_label.pack(pady=5)

# Humidity Display
humidity_label = Label(root, text="Humidity: --%", font=("Arial", 14), bg="#f0f0f0")
humidity_label.pack(pady=5)

# Status Display
status_label = Label(root, text="Status: --", font=("Arial", 14), bg="#f0f0f0")
status_label.pack(pady=5)


# Create data folder if not present
if not os.path.exists("data"):
    os.makedirs("data")

log_file = "data/weather_log.csv"

# Write header only if file is new
if not os.path.exists(log_file) or os.stat(log_file).st_size == 0:
    with open(log_file, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Temperature", "Humidity", "Timestamp", "Status"])

def get_weather():
    temp = random.randint(20, 35)
    humidity = random.randint(40, 70)

    # Determine status
    if temp > 32:
        status = "Hot 🔥"
    elif temp < 24:
        status = "Cool ❄️"
    else:
        status = "Normal 🌤️"

    # Update labels
    temp_label.config(text=f"Temperature: {temp}°C")
    humidity_label.config(text=f"Humidity: {humidity}%")
    status_label.config(text=f"Status: {status}")

    # Call this function again after 2000ms (2 sec)
    root.after(2000, get_weather)

def log_data():
    temp_text = temp_label.cget("text").split(": ")[1].replace("°C", "")
    humidity_text = humidity_label.cget("text").split(": ")[1].replace("%", "")
    status_text = status_label.cget("text").split(": ")[1]
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([temp_text, humidity_text, timestamp, status_text])

def start_logging():
    global logging_job
    log_data()
    logging_job = root.after(2000, start_logging)

def stop_logging():
    global logging_job
    if logging_job is not None:
        root.after_cancel(logging_job)
        logging_job = None
        status_label.config(text="Status: Logging stopped ⏹️")
        print("Logging stopped.")

def show_graph():
    temperatures = []
    humidities = []
    timestamps = []

    try:
        with open(log_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    temperatures.append(int(row["Temperature"]))
                    humidities.append(int(row["Humidity"]))
                    timestamps.append(row["Timestamp"])
                except ValueError:
                    # Skip bad rows (like headers accidentally logged again)
                    continue
    except FileNotFoundError:
        print("CSV file not found.")
        return

    if not temperatures:
        print("No data to show.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, label="Temperature (°C)", color="red", marker='o')
    plt.plot(timestamps, humidities, label="Humidity (%)", color="blue", marker='x')
    plt.xlabel("Timestamp")
    plt.ylabel("Value")
    plt.title("Weather Log Graph - TempTrak")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.show()

#start logging button
log_button = Button(root, text="Start Logging", command=lambda: start_logging(), bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
log_button.pack(pady=15)

# stop button
stop_button = Button(root, text="Stop Logging", command=stop_logging, bg="#f44336", fg="white", font=("Arial", 12), padx=10, pady=5)
stop_button.pack(pady=5)

#graph button
graph_button = Button(root, text="Show Graph", command=lambda: show_graph(), bg="#2196F3", fg="white", font=("Arial", 12), padx=10, pady=5)
graph_button.pack(pady=5)

get_weather()

# Run the GUI
root.mainloop()
