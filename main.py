from ctypes import windll
import os
from get_clients_location import get_clients_location 
from get_weather_data import get_weather_data
from PIL import Image
import customtkinter

# color variables
gray="white"
blue="#87CEEB"
dark_blue="#0984e3"
deg = u'\xb0'

def main():

    app = customtkinter.CTk()
    app.geometry("720x480")
    customtkinter.set_appearance_mode("dark")
    # windll.shcore.SetProcessDpiAwareness(1)

    app.title("Weather App")
    app.configure(bg=blue)

    # print(get_clients_location())

    clients_location = get_clients_location()

    # on initial load show weather data according to clients location
    weather_data = get_weather_data(clients_location)

    def update_ui():
        subheading.configure(text=f"Current Weather Conditions in {weather_data['location']['name']}, {weather_data['location']['region']}.")
        temperature_text.configure(text=f"{(weather_data['current']['temp_c'])} {deg}C")
        feels_like_temperature_text.configure(text=f"feels like {(weather_data['current']['feelslike_c'])} {deg}C")
        condition_text.configure(text=f"{(weather_data['current']['condition']['text'])}")

        # Update the image - Assuming you have a function to load the image based on the new weather data
        icon_url = weather_data["current"]["condition"]["icon"]
        icon_url_arr = icon_url.split("/")
        img_path = f"images/64x64/{icon_url_arr[-2]}/{icon_url_arr[-1]}"
        img = customtkinter.CTkImage(Image.open(img_path), size=(80, 80))
        panel.configure(image = img)

        wind_speed.configure(text=f"🎐 Wind Speed: {(weather_data['current']['wind_kph'])}kmph {(weather_data['current']['wind_dir'])}")
        pressure.configure(text=f"🌡 Pressure: {(weather_data['current']['pressure_in'])}In")
        precipitation.configure(text=f"🌧 Precipitation: {(weather_data['current']['precip_mm'])}mm")
        humidity.configure(text=f"💧 Humidity: {(weather_data['current']['humidity'])}%")
        uv.configure(text=f"☀ UV index: {(weather_data['current']['uv'])}")
        vision.configure(text=f"👁 Visibility: {(weather_data['current']['vis_km'])}km")



    def update_weather_data(query):
        if(query==""):
            return
        nonlocal weather_data 
        weather_data = get_weather_data(query)
        update_ui()
        # print(weather_data)
    
    # print(weather_data)

    # title of app
    title = customtkinter.CTkLabel(master=app, 
                                    text="Search by City or Airport Code",
                                    width=300,height=30,
                                    font=("Arial", 16), text_color=gray
                               )
    title.pack(padx=10, pady=10)

    query_var = customtkinter.StringVar()
    query_entry = customtkinter.CTkEntry(app, width=250, height=35, font=("Arial", 16),text_color=gray, textvariable=query_var)
    query_entry.place(x=175, y=50)

    icon_url = weather_data["current"]["condition"]["icon"]
    icon_url_arr = icon_url.split("/")

    search_btn = customtkinter.CTkButton(master=app,
                                    text="Search",
                                    width=100,
                                    height=35,
                                    font=("Arial", 16),
                                    fg_color=dark_blue,
                                    corner_radius=5,
                                    hover_color=dark_blue,
                                    text_color="white",
                                    command=lambda *a:update_weather_data(query_var.get()))
                
    search_btn.place(x=450, y=50)
    # print(icon_url)

    subheading = customtkinter.CTkLabel(master=app, 
                                    text=f"Current Weather Conditions in {weather_data['location']['name']}, {weather_data['location']['region']}.",
                                    height=30,
                                    font=("Arial", 16), text_color=gray
                               )
    subheading.place(x=50, y=100)

    img_path = f"images/64x64/{icon_url_arr[-2]}/{icon_url_arr[-1]}"
    img = customtkinter.CTkImage(Image.open(img_path), size=(70, 70))
    panel = customtkinter.CTkLabel(app, image = img, text="")
    
    panel.place(x=50, y=130)

    temperature_text = customtkinter.CTkLabel(master=app, 
                                    text=f"{(weather_data['current']['temp_c'])} {deg}C",
                                    font=("Arial", 32), text_color=gray
                               )
    temperature_text.place(x=135, y=145)
    feels_like_temperature_text = customtkinter.CTkLabel(master=app, 
                                                         height=12,
                                    text=f"feels like {(weather_data['current']['feelslike_c'])} {deg}C",
                                    font=("Arial", 12), text_color=gray
                               )
    feels_like_temperature_text.place(x=135, y=180)
    condition_text = customtkinter.CTkLabel(master=app, 
                                    text=f"{(weather_data['current']['condition']['text'])} ",
                                    font=("Arial", 45), text_color=gray
                               )
    condition_text.place(x=260, y=140)

    wind_speed = customtkinter.CTkLabel(master=app, 
                                    text=f"🎐 Wind Speed: {(weather_data['current']['wind_kph'])}kmph {(weather_data['current']['wind_dir'])}",
                                    font=("Arial", 16), text_color=gray)
    wind_speed.place(x=50, y=210)

    pressure = customtkinter.CTkLabel(master=app, 
                                    text=f"🌡 Pressure: {(weather_data['current']['pressure_in'])}In",
                                    font=("Arial", 16), text_color=gray)
    pressure.place(x=50, y=235)

    precipitation = customtkinter.CTkLabel(master=app, 
                                    text=f"🌧 Precipitation: {(weather_data['current']['precip_mm'])}mm",
                                    font=("Arial", 16), text_color=gray)
    precipitation.place(x=50, y=260)
    humidity = customtkinter.CTkLabel(master=app, 
                                    text=f"💧 Humidity: {(weather_data['current']['humidity'])}%",
                                    font=("Arial", 16), text_color=gray)
    humidity.place(x=50, y=285)
    uv = customtkinter.CTkLabel(master=app, 
                                    text=f"☀ UV index: {(weather_data['current']['uv'])}",
                                    font=("Arial", 16), text_color=gray)
    uv.place(x=50, y=310)

    vision = customtkinter.CTkLabel(master=app, 
                                    text=f"👁 Visibility: {(weather_data['current']['vis_km'])}km",
                                    font=("Arial", 16), text_color=gray)
    vision.place(x=50, y=310)

    app.mainloop()





if __name__ == "__main__":
    main()
