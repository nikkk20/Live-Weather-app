#libraries 
import requests
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def apiget(location):
    myapi = "36c140b1321fdedc00e3015b028aae5f"
    apilink = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+myapi
    link = requests.get(apilink)
    apidata = link.json()
    if apidata["cod"]=="404":
        pass
    else :
        temp_city = ((apidata['main']['temp']) - 273.15)
        weather_desc = apidata['weather'][0]['description']
        hmdt = apidata['main']['humidity']
        wind_spd = apidata['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        city = location.title()
        time = date_time
        temp = "{:.1f}°C".format(temp_city)
        weather = weather_desc.title()
        wind = "Winds:" + str(wind_spd) + 'Kmph'
        humid = "Humidity:" + str(hmdt) + '%'   
        data = (city, time, weather, temp, wind, humid)
        print(data)
        return data
        
def search():
    location = input_location.get()
    info = apiget(location)
    if info:
        city_label['text'] = '{}'.format(info[0])
        temp_label['text'] = '{}'.format(info[3])
        weather_label['text'] = '{}'.format(info[2])
        wind_label['text'] = '{}'.format(info[4])
        humid_label['text'] = '{}'.format(info[5])
        time_label['text'] = '{}'.format(info[1])  
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(location))

#main window
window = Tk()
window.title("Live Weather App")
window.geometry("1280x720")
window.resizable(0,0)
window.iconbitmap('e:\\py\\project\\data\\icon.ico') 
bck = Image.open('E:\\py\\project\\data\\bck.jpg')
base = ImageTk.PhotoImage(bck)
base_label= Label(window, image=base)


#inputtext box
location = ""
input_location = Entry(window , textvariable=location, width=50, borderwidth=5)

#output boxes
city_label = Label(window, text="", bg="#231f20", fg="white", font=('bold', 72))
time_label = Label(window, text="", bg="#231f20", fg="white", font=('bold', 24))
weather_label = Label(window , text="", bg="#231f20", fg="white", font=('bold', 17))
temp_label = Label(window, text="", bg="#231f20", fg="white", font=('bold', 60))
wind_label = Label(window, text="", bg="#231f20", fg="white", font=('bold', 17))
humid_label = Label(window, text="", bg="#231f20", fg="white", font=('bold', 17))

#buttons
button_search = Button(window, text="Search", command=search)

#locations
base_label.place(x=0, y=0)
input_location.place(x=498, y=39)
button_search.place(x=632, y=65)
city_label.place(x=438, y=333)
time_label.place(x=438, y=613)
weather_label.place(x=720, y=460)
temp_label.place(x=438, y=460)
wind_label.place(x=720, y=523)
humid_label.place(x=720, y=490)


window.mainloop()
