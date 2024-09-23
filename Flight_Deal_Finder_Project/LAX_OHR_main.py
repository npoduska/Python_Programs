"""This program is supposed to get the 5 cheapest round trip, nonstop flights within a date range.
Don't think it's working accurately. It gets fixated on a price and time and just repeats it.  
Program needs improvement in having it search a broader range of dates.  But using the APIs work tho!"""

import requests
from datetime import datetime, timedelta
import config


def get_access_token(api_key, api_secret):
    response = requests.post(
        config.TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": api_key,
            "client_secret": api_secret,
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]

def search_flights(access_token, origin, destination, departure_date, return_date):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "returnDate": return_date,
        "adults": 1,
        "nonStop": "true",
        "currencyCode": "USD",
        "max": 5  # Limit to top 5 results
    }
    response = requests.get(config.FLIGHT_SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def main():
    # Load API credentials
    api_key = config.AMADEUS_API_KEY
    api_secret = config.AMADEUS_SECRET

    # Generate access token
    access_token = get_access_token(api_key, api_secret)

    # Set up date parameters
    today = datetime.now()
    departure_date = (today + timedelta(days=25)).strftime("%Y-%m-%d")
    return_date = (today + timedelta(days=35)).strftime("%Y-%m-%d")  # 10 days after departure
    
    # Search for round-trip flights
    results = search_flights(access_token, "LAX", "ORD", departure_date, return_date)

    # Process and display results
    print(f"Top 5 cheapest round-trip flights from LAX to ORD:")
    print(f"Departure: {departure_date}, Return: {return_date}")
    for i, offer in enumerate(results.get("data", [])[:5], 1):
        price = offer["price"]["total"]
        outbound = offer["itineraries"][0]["segments"][0]
        inbound = offer["itineraries"][1]["segments"][0]
        print(f"{i}. Price: ${price}")
        print(f"   Outbound: {outbound['departure']['iataCode']} to {outbound['arrival']['iataCode']} - {outbound['departure']['at']}")
        print(f"   Inbound: {inbound['departure']['iataCode']} to {inbound['arrival']['iataCode']} - {inbound['departure']['at']}")
        print()

if __name__ == "__main__":
    main()