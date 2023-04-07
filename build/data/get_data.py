# SCRIPT NAME: Get Data
# DEFINITION: 
# AUTHOR: JTA
# LAST MODIFIED: april 5th, 2023

#Libraries
import os #file management
from dotenv import load_dotenv, find_dotenv #load secrets
import pyowm #OpenWeather wrap up

#Functions
def getSecrets()->None:
    """
    # Definition
    Loads env variables from .env file
    # Parameters
    - path(str): path to .env file
    # Return
    None
    """
    load_dotenv(find_dotenv()) #searches and loads .env file into runtime
    secrets = {"API_KEY":os.environ.get("API_KEY"),
               "DB_USER":os.environ.get("DB_USER"),
               "DB_PSW":os.environ.get("DB_PSW"),
               "DB_HOST":os.environ.get("DB_HOST"),
               "DB_PORT":os.environ.get("DB_PORT")}
    
    return secrets

#Main Process
start_date = "1/01/2023"
end_date = "1/04/2023"
secrets = getSecrets() #Loads env variables

owm = pyowm.OWM('API_KEY')
weather_mgr = owm.weather_manager()
place = 'Monterrey, MX'
observation = weather_mgr.weather_at_place(place)

history = weather_mgr.weather_history_at_place(place, start_date, end_date)
history_list = history.get_weathers()
for weather in history_list:
    temperature = weather.get_temperature('celsius')
    humidity = weather.get_humidity()
    wind = weather.get_wind()
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
    print(f'Wind Speed: {wind["speed"]} m/s')