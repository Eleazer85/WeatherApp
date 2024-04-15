import requests
import json
from geopy.geocoders import Nominatim
import geocoder
import tkintermapview
import customtkinter
from PIL import Image

API_KEY = "API_KEY"

class weatherApps():
    def __init__(self) -> None:
        
        g = geocoder.ip('me')
        LATITUDE = g.latlng[0]
        LONNGTUDE =  g.latlng[1]

        print(LATITUDE)
        print(LONNGTUDE)
        
        api = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONNGTUDE}&appid={API_KEY}")
        api = json.loads(api.content)
        
        """This commented code is used to know the structure"""
        # with open("weather.json","r") as f:
        #     api = json.load(f)
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root = customtkinter.CTk()
        self.root.title("Weather App")
        self.root.geometry("1200x600")
        
        #create tabview
        self.tab = customtkinter.CTkTabview(master=self.root,width=600,height=200)
        self.tab.grid(row=1,column=0,padx=70,pady=20)
        
        #create tab
        self.tab1 = self.tab.add("Information")
        
        #create map
        self.map = tkintermapview.TkinterMapView(self.root, width=600, height=300)
        self.map.set_position(LATITUDE, LONNGTUDE)
        self.map.set_marker(LATITUDE, LONNGTUDE , text=f"Your Location\nIP Adress: {g.ip}\nLatitude: {LATITUDE}\nLongitude: {LONNGTUDE}")
        self.map.grid(row=0,column=0,padx=10,pady=30)
        
        #add and style a label
        self.label_city = customtkinter.CTkLabel(master=self.tab1, text="Enter City / Subdistrict Name:",font=("Times New Roman",20),text_color="White")
        self.label_city.grid(row=1,column=0,padx=(85,0),pady=(30,0))
        
        #add an entry
        self.input_city = customtkinter.CTkEntry(master=self.tab1,width=200,height=30,font=("Times New Roman",20))
        self.input_city.grid(row=1,column=1,padx=10,pady=(30,0))
        
        self.input_submit = customtkinter.CTkButton(master=self.tab1,text="Submit",width=100,height=30,font=("Times New Roman",20),command=self.Change_loc)
        self.input_submit.place(relx=0.5,rely=0.7,anchor="center")
        
        self.tab_info = customtkinter.CTkTabview(master=self.root,width=500,height=0)
        self.tab_info.place(relx=0.565,rely=0.26,anchor="w")
        self.tabinf = self.tab_info.add("Main Data")
        
        self.info_weather = customtkinter.CTkLabel(master=self.tabinf,text=f"{api['weather'][0]['main']}",font=("Times New Roman",50),text_color="White")
        self.info_weather.grid(row=0,column=0,pady=(0,0),padx=(30,0))
        
        self.info_temp = customtkinter.CTkLabel(master=self.tabinf,text=f"{round(api['main']['temp']-273.15)} °C / {round(((api['main']['temp']-273.15)*9)/5)} °F",font=("Times New Roman",50),wraplength=200,text_color="White")
        self.info_temp.place(relx=0.6,rely=0.35,anchor="w")
    
        if api["weather"][0]["main"] == "Rain":
            self.info_symbol = customtkinter.CTkImage(light_image=Image.open("raining.png"),dark_image=Image.open("raining.png"),size=(200,140))
            # Create a label to display the image
            self.image_label = customtkinter.CTkLabel(master=self.tabinf, image=self.info_symbol)
            self.image_label.grid(row=1, column=0,padx=(30,0),pady=(0,50))  # Adjust the row and column as needed
        elif api["weather"][0]["main"] == "Haze":
            self.info_symbol = customtkinter.CTkImage(light_image=Image.open("haze.png"),dark_image=Image.open("haze.png"),size=(200,140))
            # Create a label to display the image
            self.image_label = customtkinter.CTkLabel(master=self.tabinf, image=self.info_symbol)
            self.image_label.grid(row=1, column=0,padx=(30,0),pady=(0,50))  # Adjust the row and column as needed
        elif api["weather"][0]["main"] == "Clouds":
            self.info_symbol = customtkinter.CTkImage(light_image=Image.open("clouds.png"),dark_image=Image.open("clouds.png"),size=(200,140))
            # Create a label to display the image
            self.image_label = customtkinter.CTkLabel(master=self.tabinf, image=self.info_symbol)
            self.image_label.grid(row=1, column=0,padx=(30,0),pady=(0,50))  # Adjust the row and column as needed
        elif api["weather"][0]["main"] == "Clear":
            self.info_symbol = customtkinter.CTkImage(light_image=Image.open("clear.png"),dark_image=Image.open("clouds.png"),size=(200,140))
            # Create a label to display the image
            self.image_label = customtkinter.CTkLabel(master=self.tabinf, image=self.info_symbol)
            self.image_label.grid(row=1, column=0,padx=(30,0),pady=(0,50))  # Adjust the row and column as needed
            
        self.tab_other = customtkinter.CTkTabview(master=self.root,width=500,height=300)
        self.tab_other.place(relx=0.565,rely=0.72,anchor="w")
        self.other = self.tab_other.add("Other Data")
        
        self.city = customtkinter.CTkLabel(master=self.other,text=f"City / Subdistrict: {api['name']}",font=("Times New Roman",20),text_color="White")
        self.city.grid(row=0,column=0,padx=(5,130) , pady=(40,10))
        
        self.info_humid = customtkinter.CTkLabel(master=self.other,text=f"Humidity: {api['main']['humidity']} %",font=("Times New Roman",20),text_color="White")
        self.info_humid.grid(row=1,column=0,padx=(8,110) , pady=(0,10))
        
        self.Pressure = customtkinter.CTkLabel(master=self.other,text=f"Pressure: {api['main']['pressure']} hPa",font=("Times New Roman",20),text_color="White")
        self.Pressure.grid(row=2,column=0,padx=(20,100) , pady=(0,10))
        
        self.Wind_spd = customtkinter.CTkLabel(master=self.other,text=f"Wind speed: {api['wind']['speed']} m/s",font=("Times New Roman",20),text_color="White")
        self.Wind_spd.grid(row=3,column=0,padx=(20,82) , pady=(0,10))
        
        self.Wind_direction = customtkinter.CTkLabel(master=self.other,text=f"Wind direction: {api['wind']['deg']}°",font=("Times New Roman",20),text_color="White")
        self.Wind_direction.grid(row=4,column=0,padx=(36,100) , pady=(0,10))
        
        self.root.mainloop()
    
    def error(self,error_message):
        error_popup = customtkinter.CTkToplevel(self.root)
        error_popup.grab_set()
        error_popup.geometry("400x130")
        error_popup.title("Error")
        
        error_label = customtkinter.CTkLabel(master=error_popup,wraplength=330,text=error_message,font=("Times New Roman",20),text_color="White")
        error_label.pack(pady=(30,0))
        
        ok_button = customtkinter.CTkButton(master=error_popup,text="OK",width=50,height=30,font=("Times New Roman",20),command=error_popup.destroy)
        ok_button.pack(pady=10)
        
    def Change_loc(self):
        city_name = self.input_city.get()
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(city_name)
        
        if location == None: 
            self.error(f"No City called {city_name} was found, please check again")
        else: 
            api = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={API_KEY}")
            api = json.loads(api.content)
            
            self.city.configure(text=f"City / Subdistrict: {city_name} , {api['name']}")
            self.info_humid.configure(text=f"Humidity: {api['main']['humidity']} %")
            self.Pressure.configure(text=f"Pressure: {api['main']['pressure']} hPa")
            self.Wind_spd.configure(text=f"Wind speed: {api['wind']['speed']} m/s")
            self.Wind_direction.configure(text=f"Wind direction: {api['wind']['deg']}°")
            
            self.map.set_position(location.latitude,location.longitude)
            self.map.set_marker(location.latitude,location.longitude,text=f"Your Location\nLatitude: {location.latitude}\nLongitude: {location.longitude}")
            
            self.info_temp.configure(text=f"{round(api['main']['temp']-273.15)} °C / {round(((api['main']['temp']-273.15)*9)/5)} °F",font=("Times New Roman",50),wraplength=200,text_color="White")
            self.info_weather.configure(text=f"{api['weather'][0]['main']}")
            
            if api["weather"][0]["main"] == "Rain": 
                self.info_symbol.configure(light_image=Image.open("raining.png"),dark_image=Image.open("raining.png"),size=(200,140))
                self.image_label.configure(image=self.info_symbol)
            elif api["weather"][0]["main"] == "Haze": 
                self.info_symbol.configure(light_image=Image.open("haze.png"),dark_image=Image.open("haze.png"),size=(200,140))
                self.image_label.configure(image=self.info_symbol)
            elif api["weather"][0]["main"] == "Clouds": 
                self.info_symbol.configure(light_image=Image.open("clouds.png"),dark_image=Image.open("clouds.png"),size=(200,140))
                self.image_label.configure(image=self.info_symbol)
            elif api["weather"][0]["main"] == "Clear": 
                self.info_symbol.configure(light_image=Image.open("clear.png"),dark_image=Image.open("clear.png"),size=(200,140))
                self.image_label.configure(image=self.info_symbol)

if __name__ == "__main__":
    weatherApps()