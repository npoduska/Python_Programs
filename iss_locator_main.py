"""This program answers the tough question; can I see the International Space Station now? 
When can I see it based on my location? Where is ISS right now? And when could I see in the near
future? This program calls several API sources to help answer these questions to help you 
catch a glimpse of that awesome ISS!
*Improvements are planned for the future. This code will probably be reformatted. Performance improvements will
be sought out. Error handling will be handled better. Maybe even a GUI will be added. IDK. Someday.
But no new features are planned to be added, as all the important questions have been answered."""

#-------------------IMPORTS---------------------------------
import requests, json
from config import *
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from datetime import datetime
from timezonefinder import TimezoneFinder
import pytz
import feedparser


#------------------INPUT YOUR LOCATION, CONVERT IT TO LAT/LONG COORDINATES---------------------------------
#Enter your location
# COUNTRY = "Australia"
# CITY = "Sydney"
# REGION = "" #Leave blank if there is no state or region to input
# COUNTRY = "United_States"
# REGION = "Illinois" #State
# CITY = "Chicago"
COUNTRY = "United_States"
REGION = "Colorado" #State
CITY = "Denver"

#First get the coordinates of location
# Create a geolocator object with a user-defined app name
geolocator = Nominatim(user_agent= USER_AGENT)

# Format the location string
location_str = f"{CITY}, {REGION}, {COUNTRY}"

try:
    # Get the location
    location = geolocator.geocode(location_str)
    
    if location:
        # Extract latitude and longitude
        country_lat = location.latitude
        country_long = location.longitude
        print(f"City Latitude: {country_lat}")
        print(f"City Longitude: {country_long}")
    else:
        print("Location not found.")
except GeocoderTimedOut:
    print("Geocoding service timed out. Please try again later.")

#-------------------FIND WHEN IT IS DARK AT YOUR LOCATION, AND WHAT IS THE CURRENT TIME AT THAT LOCATION---------------------------------
parameters = {
    "lat": country_lat,
    "lng": country_long,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

def get_current_time_by_coordinates(latitude, longitude):
    # Initialize TimezoneFinder
    tf = TimezoneFinder()

    # Get the timezone string from the coordinates
    time_zone_str = tf.timezone_at(lat=latitude, lng=longitude)

    if not time_zone_str:
        return "Timezone not found for the given coordinates."

    # Get the timezone object
    time_zone = pytz.timezone(time_zone_str)

    # Get the current time in that timezone
    current_time = datetime.now(time_zone)

    return current_time.strftime('%Y-%m-%d %H:%M:%S')
    
current_time = get_current_time_by_coordinates(country_lat,country_long)

#The localized time at the given location. First it changes over to lat/long coordinates, then goes through timezone stuff, and spits out the local date and time.
# print(current_time)

# Convert the string to a datetime object
timestamp = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

# Extract individual components
current_month = timestamp.month
current_day = timestamp.day
hour = timestamp.hour
minute = timestamp.minute
# Print the results
# print(f"Month: {current_month}")
# print(f"Day: {current_day}")
# print(f"Hour: {hour}")
# print(f"Minute: {minute}")

#-------------------GET ISS CURRENT COORDINATES---------------------------------
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_point = (iss_latitude, iss_longitude)

#-------------------DETERMINE IF YOU CAN SEE ISS RIGHT NOW. IS IT CLOSE TO ME? IS IT DARK ENOUGH OUTSIDE?-------
#Check if ISS is located close to my current location, and it is dark outside. Reformat this...
if country_lat - 5 <= iss_latitude <= country_lat + 5:
    print("Latitude is good.")
    if country_long - 5 <= iss_longitude <= country_long + 5:
        print("Longitude is good.")
        if sunset <= current_time <= sunrise:
            print("You should be able to see ISS above you now!")

#-------------------IF I CAN'T SEE IT NOW, WHERE IN THE WORLD IS ISS??---------------------------------
try:
    # Perform reverse geocoding
    location = geolocator.reverse((iss_latitude, iss_longitude), exactly_one=True, language='en')
    
    if location:
        # Extract the address components
        address = location.raw['address']
        
        # Retrieve the closest city, state, country, and body of water if available
        city = address.get('city', 'Not available')
        state = address.get('state', 'Not available')
        country = address.get('country', 'Not available')
        body_of_water = address.get('water', 'Not available')  # Body of water is not always available
        
        # Print the results
        print("Here is where ISS is currently located in the world...")
        print(f"City: {city}")
        print(f"State: {state}")
        print(f"Country: {country}")
        print(f"Body of Water: {body_of_water}")
    # else:
    #-------------------------------Determine if ISS is over water or land.-------------------------------------
    import http.client
    conn = http.client.HTTPSConnection("isitwater-com.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': X_RAPIDAPI_KEY,
        'x-rapidapi-host': X_RAPIDAPI_HOST,
    }
    conn.request("GET", f"/?latitude={iss_latitude}&longitude={iss_longitude}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    data = json.loads(data)

    if (data["water"]):
        print("ISS is over a body of water.")
    else:
        print("ISS is over land.")
    # print("Location not found.")
except GeocoderTimedOut:
    print("Geocoding service timed out. Please try again later.")

#Report where ISS is right now...
key = API_KEY
print(f"https://geocode.xyz/{iss_latitude},{iss_longitude}?geoit=json&auth={key}")
# print(f"https://geocode.xyz/{latitude},{longitude}?geoit=xml&auth={key}")
response = requests.get(f"https://geocode.xyz/{iss_latitude},{iss_longitude}?geoit=json&auth={key}")
# response = requests.get(f"https://geocode.xyz/{latitude},{longitude}?geoit=xml&auth={key}")
response.raise_for_status()
data = response.json()
iss_point = (iss_latitude, iss_longitude)

# print(data)

if "suggestion" in data:  #If there is an error, 'suggestion' in the data will not be available. This checks if suggestion exists.
    iss_region = str(data["suggestion"]["region"])
    iss_subregion = str(data["suggestion"]["subregion"])
    iss_territory = str(data["suggestion"]["territory"])
    iss_altname = str(data["suggestion"]["altname"])
else:
    iss_region = str(data.get("region", "Region not available"))
    iss_subregion = str(data.get("subregion", "Subregion not available"))
    iss_territory = str(data.get("territory", "Territory not available"))
    iss_altname = str(data.get("altname", "Altname not available"))

print(f"Current ISS Coordinates: {iss_point}")
print(f"ISS Territory Location: {iss_territory}")
print(f"ISS Altname Location: {iss_altname}")
print(f"ISS Region Location: {iss_region}")
print(f"ISS Subregion Location: {iss_subregion}")

#-------------------WHEN SHOULD I BE ABLE TO SEE IT IN THE FUTURE??---------------------------------
#--------------Output the information for future sightings based on the location given. -------------------------------
NewsFeed = feedparser.parse(f"https://spotthestation.nasa.gov/sightings/xml_files.cfm?filename={COUNTRY}_{REGION}_{CITY}.xml")
# entry = NewsFeed.entries[0]
# entry = NewsFeed.entries[]
# print (NewsFeed)
# print (entry)

print ('Number of RSS posts :', len(NewsFeed.entries))

#dict_keys(['title', 'title_detail', 'published', 'published_parsed', 'summary', 'summary_detail', 'id', 'guidislink', 'link'])

print(f"Here is when you can see ISS from {CITY}, {REGION}, {COUNTRY}:")
len_entries = len(NewsFeed.entries)
if len_entries ==0:
    print("No near future sightings available at this moment.")
# if len_entries > 6:
#     len_entries = 5
for i in range(0,len_entries):
    entry = NewsFeed.entries[i]
    # Extract the date from the title (format: YYYY-MM-DD)
    try:
        title_date_str = entry.title.split(' ')[0]
        title_date = datetime.strptime(title_date_str, "%Y-%m-%d")
        
        # Compare the extracted month and day with the current month and day. We only want to print future sightings.
        if title_date.month > current_month or (title_date.month == current_month and title_date.day > current_day):
            entry_text = entry.title
            summary_text = entry.summary
            print ('Title :',entry_text.replace("<br />", "")) #Cleaning up the text, removing "<br />"
            print ('Summary :',summary_text.replace("<br />", ""))  # Future sightings info
    except ValueError:
        # In case the date format is wrong, just return False
        print("Date is in wrong format")
    
