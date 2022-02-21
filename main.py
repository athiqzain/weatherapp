import tkinter as tk
import requests
import time


def weather(canvas):
    city = cityname.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=00b7eb9c3c6ef90a5896a764d9dab5c7"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    humidity = json_data['main']['humidity']


    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Humidity: " + str(humidity)
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Weather App")
font1 = ("poppins", 40, "bold")
font2 = ("poppins", 20, "bold")


cityname = tk.Entry(canvas, width=20, font=font1)
cityname.pack(pady=50)
cityname.bind('<Return>', weather)

label1 = tk.Label(canvas, font=font1)
label1.pack()
label2 = tk.Label(canvas, font=font2)
label2.pack()
canvas.mainloop()