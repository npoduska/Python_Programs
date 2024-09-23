"""This program is supposed to find the lowest prices between a couple of dates. It 
looks for routes from our origin airport to other places 
that we can specify in a google sheet. 
This program blows up in which it is supposed to send out alerts via emails or SMS messages to 
all people that signed up via google form that we connected to our google sheet. 
There's lots of moving parts jumping from one resource to the next. 
This specific code does not send out alerts. I don't think it even finds the lowest price 
in between dates (it just searches on specific dates!). It /works/ without errors. Maybe not as intended.
But here you go."""

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# Set your origin airport
ORIGIN_CITY_IATA = "OHR"


# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Retrieve your customer emails ====================

customer_data = data_manager.get_customer_emails()
# Verify the name of your email column in your sheet. Yours may be different from mine
customer_email_list = [row["email"] for row in customer_data]
print(f"Your email list includes {customer_email_list}")

# ==================== Search for direct flights  ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting direct flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: ${cheapest_flight.price}")

    # ==================== Send Notifications and Emails  ====================
    # Nope. Not doing this. The program is a monster as it is...