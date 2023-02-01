from tkinter import *
import requests
import json


root = Tk()
root.title("Always leaning")
root.geometry("400x200")


#zip = Entry(root)
#zip.pack()
#wakaflaka = zip.get()
def zip_lookup():
#    zip.get()
#    ziplabel = Label(root, text=zip.get())
#    ziplabel.pack()
    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07670&distance"
            "=5&API_KEY=8A2CE151-127D-4837-99DF-912DCAFDD75D")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"
        root.configure(background=weather_color)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
                        background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."


# zip = Entry(root)
# zip.pack()
# zipButton = Button(root, text="Lookup Zipcode", command=zip_lookup)
# zipButton.pack()

try:
    api_request = requests.get(
        "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07670&distance"
        "=5&API_KEY=8A2CE151-127D-4837-99DF-912DCAFDD75D")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
        weather_color = "#0C0"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#ff9900"
    elif category == "Unhealthy":
        weather_color = "#FF0000"
    elif category == "Very Unhealthy":
        weather_color = "#990066"
    elif category == "Hazardous":
        weather_color = "#660000"
    root.configure(background=weather_color)
    myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
                    background=weather_color)
    myLabel.grid(row=1, column=0, columnspan=2)
except Exception as e:
    api = "Error..."

root.mainloop()