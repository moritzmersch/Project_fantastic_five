"""
This script can be used to fetch the weather data of any city in Germany using the Meteostat package.
The user has to input the name of the city as well as the start and end date of the desired period.
The resulting weather data is displayed and saved as a CSV file with the given city name.
"""

# Import the required packages
from pathlib import Path
from datetime import datetime
from geopy.geocoders import Nominatim
from meteostat import Point, Daily

# Set data path as well as start and end date
DATA_PATH = Path('Data')
START_DATE = datetime(year=2014, month=1, day=1)
END_DATE = datetime(year=2021, month=12, day=31)

# Ask the user to input the city
city = input('Which city should be fetched? >> ')

# Get the geolocation of the city
location = Nominatim(user_agent='TechLabs').geocode(city)
latitude, longitude = location.latitude, location.longitude

# Create the Meteostat request and fetch the data
request = Daily(loc=Point(lat=latitude, lon=longitude), start=START_DATE, end=END_DATE)
weather_data = request.fetch().reset_index()

# Save the data with the given path and city name
weather_data.to_csv(path_or_buf=DATA_PATH.joinpath(f'Weather_{city.title()}.csv'), index=False)

# Display the first 15 rows of the fetched data
print(weather_data.head(15))
