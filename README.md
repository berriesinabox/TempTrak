🌡️ TempTrak – Weather Simulator & Logger App
TempTrak is a desktop GUI application built with Python that simulates weather data (temperature and humidity), logs the information into a .csv file, and visualizes it using Matplotlib all through a simple and intuitive Tkinter interface.

🔧 Features
Real-time weather simulation using random values

Start/Stop logging temperature, humidity, timestamp & weather status to CSV

Visualize logged data using line graphs with Matplotlib

Manual reset to start fresh data each session

🚀 How to Run
Requirements

Python 3.x

matplotlib (Install using pip install matplotlib)

Steps

Clone/download this repository

Run temptrak.py using Python
Example: python temptrak.py

The GUI will open:

Click Start Logging to begin

Click Stop Logging to stop data collection

Click Show Graph to visualize the data collected in the current session

Note: Make sure the data/ folder exists (created automatically on first run) to store the log CSV.

📁 File Structure
TempTrak/
├── data/
│ └── weather_log.csv (stores logged data)
│ └── sample-weather-graph.png (optional graph image)
├── temptrak.py (main GUI script)
├── README.md (project description)

🛠️ Built With
Python

Tkinter

Matplotlib

CSV module

Random, time, os (standard Python libraries)

💬 Credits
This project was built as a hands-on learning experiment in GUI development.
Many helpful nudges came from AI along the way but every line was explored, tested, and built with care.

📌 Future Improvements
Auto-clear previous CSV data at the start of each session

Add UI styling themes

Export graph as image from the GUI itself

Replace random data with real API weather data

🙋‍♀️ About Me
Hi! I’m Shivangi, a first-year student exploring Python, GUI development, and building fun projects like this as part of my learning journey. Feel free to connect! 💙
