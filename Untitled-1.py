import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os
import requests

# Load environment variables from the .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set the 'OPENWEATHER_API_KEY' environment variable.")

# Function to fetch weather data
def get_weather():
    city = city_entry.get()  # Get city name from input field
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            result_label.config(text=f"Temperature: {temp}°C\nDescription: {desc}")
        else:
            messagebox.showerror("Error", f"City not found or API error ({response.status_code})")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

# Create input label and entry box
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Create button to fetch weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Label to display results
result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
