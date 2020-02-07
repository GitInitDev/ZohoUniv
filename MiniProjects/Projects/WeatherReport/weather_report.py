import tkinter as tk
import requests
import json
win = tk.Tk()
win.title("Weather Report")
win.geometry("800x800")
api = "your API"
url = "http://api.openweathermap.org/data/2.5/weather?"
def weather () :
    location = entry.get()
    answer = url + "appid=" +api + "&q=" +location
    response = requests.get(answer)
    res = response.json()
    if res["cod"] !="404" :
        x = res["main"]
        temperature = x["temp"]
        pressure = x["pressure"]
        humidity = x["humidity"]
        y = res["weather"]
        weather_detail = y[0]["description"]
        label1 = tk.Label(win , text = 'Temperature (In Kelvin) = {temp} , \n'' Atmospheric Pressure (In hPa) = {pre} , \n'' Humidity (In Percentage) = {hum} , \n'' Detail = {weather_detail} ')
        label1.grid(row = 2 , column = 0)
    else :
        label2 = tk.Label(win , text = "Enter The Correct Location")
        label2.grid(row = 2 , column = 0)
label = tk.Label(win , text = "Enter Location : " , bg = "#009332")
label.grid(row = 0 , column = 0)
label.config(font=("=sans serif" , 20 , "bold"))
entry = tk.Entry(win)
entry.grid(row = 1 , column = 0 , padx = 100)
button = tk.Button(win , text = "Search" , command = weather)
button.grid(row = 1 , column = 1)
win.mainloop()
