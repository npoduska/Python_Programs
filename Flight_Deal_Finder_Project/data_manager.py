import os
import requests
from requests.auth import HTTPBasicAuth
# from dotenv import load_dotenv #Get your own keys
from config import SHEETY_USERNAME, SHEETY_PASSWORD, SHEETY_PRICES_ENDPOINT, SHEETY_USERS_ENDPOINT #Get your own keys

# Load environment variables from .env file
# load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self._user = os.environ["SHEETY_USERNAME"]
        # self._password = os.environ["SHEETY_PASSWORD"]
        self._user = SHEETY_USERNAME
        self._password = SHEETY_PASSWORD
        self.prices_endpoint = SHEETY_PRICES_ENDPOINT
        self.users_endpoint = SHEETY_USERS_ENDPOINT
        self.authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self.authorization)
        print("Status Code:", response.status_code)
        response.raise_for_status()
        data = response.json()
        print("Raw API response:", data)
        
    
    # Check if 'prices' key exists, if not, use the first key in the dictionary
        if 'prices' in data:
            self.destination_data = data["prices"]  #'prices' is the sheet's name
        else:
            # If 'prices' doesn't exist, use the first key in the dictionary
            first_key = next(iter(data))
            print(f"'prices' key not found. Using '{first_key}' instead.")
            self.destination_data = data[first_key]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                auth=self.authorization,
                json=new_data
            )
            print(response.text)
            
    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, auth=self.authorization)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        # print(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data