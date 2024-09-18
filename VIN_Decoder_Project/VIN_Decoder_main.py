"""This program allows you to take a picture of a car's VIN, then run that VIN through vindecoder.eu API 
to collect info about that car. Such info as: packages installed in vehicle, type of engine, if vehicle
was stolen, the market value of car, as well as account balance of how many more lookups you have left 
with vindecoder.eu API."""

import requests, hashlib, json
from config import API_KEY, SECRET_KEY, IMAGE_API_KEY   #Get your own keys

#----------------Convert VIN image to VIN text string OR manually write in the VIN---------------
#(Optional) write in the VIN below:
vin_text= ''
#--------------------------------

# Your API key (use 'helloworld' for a free key). Using https://ocr.space/
api_key = IMAGE_API_KEY

# Path to the image you want to extract text from
#Accepts .png,.jpg,.webp or .PDF files
image_path ='vin_image1.jpg'

if image_path is None:
    print(f"Error: Could not load image from {image_path}")
else:
        
    # Upload the image and send it to the API
    with open(image_path, 'rb') as image_file:
        response = requests.post(
            'https://api.ocr.space/parse/image',
            files={'image': image_file},
            data={
                'apikey': api_key,      # Your API key
                'language': 'eng',      # Language of the image text
                'isOverlayRequired': False  # No need for text overlay on the image
            }
        )
    # Get the result in JSON format
    result = response.json()
    # Check for errors
    if result['IsErroredOnProcessing']:
        print("Error:", result['ErrorMessage'][0])
    else:
        # Extract and print the parsed text
        vin_text = result['ParsedResults'][0]['ParsedText']
        print("Extracted Text:")
        print(vin_text)

#---------------------------------------------------------------------------------

VIN_API_KEY = API_KEY
VIN_SECRET_KEY = SECRET_KEY
VIN= vin_text
vin_endpoint = "https://api.vindecoder.eu/3.2"

#VIN Decode Info
ID= "decode"

controlSum = hashlib.sha1((VIN.upper()+"|"+ID+"|"+VIN_API_KEY+"|"+VIN_SECRET_KEY).encode('utf-8')).hexdigest()[:10]
url = vin_endpoint+"/"+VIN_API_KEY+"/"+controlSum+"/"+ID+"/"+VIN.upper()+".json"
print(url)
json_data = requests.get(url).json()
# print(json_data)

# Convert the data to a pretty-printed JSON format and write it to a text file
with open("decode_output.txt", "w") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
print("Pretty decode_output JSON data has been written to decode_output.txt")

#VIN Stolen Check Info
ID= "stolen-check"

controlSum = hashlib.sha1((VIN.upper()+"|"+ID+"|"+VIN_API_KEY+"|"+VIN_SECRET_KEY).encode('utf-8')).hexdigest()[:10]
url = vin_endpoint+"/"+VIN_API_KEY+"/"+controlSum+"/"+ID+"/"+VIN.upper()+".json"
print(url)
json_data = requests.get(url).json()
# print(json_data)

# Convert the data to a pretty-printed JSON format and write it to a text file
with open("stolen_check_output.txt", "w") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
print("Pretty stolen_check_output JSON data has been written to stolen_check_output.txt")

#Vehicle Market Value Info
ID= "vehicle-market-value"

controlSum = hashlib.sha1((VIN.upper()+"|"+ID+"|"+VIN_API_KEY+"|"+VIN_SECRET_KEY).encode('utf-8')).hexdigest()[:10]
url = vin_endpoint+"/"+VIN_API_KEY+"/"+controlSum+"/"+ID+"/"+VIN.upper()+".json"
print(url)
json_data = requests.get(url).json()
# print(json_data)

# Convert the data to a pretty-printed JSON format and write it to a text file
with open("vehicle_market_value_output.txt", "w") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
print("Pretty stolen_check_output JSON data has been written to vehicle_market_value_output.txt")

#OEM VIN Lookup Info.............ONLY AVAILABLE FOR PAID USERS.....................
ID= "oem"

controlSum = hashlib.sha1((VIN.upper()+"|"+ID+"|"+VIN_API_KEY+"|"+VIN_SECRET_KEY).encode('utf-8')).hexdigest()[:10]
url = vin_endpoint+"/"+VIN_API_KEY+"/"+controlSum+"/"+ID+"/"+VIN.upper()+".json"
print(url)
json_data = requests.get(url).json()
# print(json_data)

# Convert the data to a pretty-printed JSON format and write it to a text file
with open("oem_output.txt", "w") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
print("Pretty stolen_check_output JSON data has been written to oem_output.txt")

#Get API account balance Info. How many more VINs are allowed to be ran through their system.
ID= "balance"

controlSum = hashlib.sha1((ID+"|"+VIN_API_KEY+"|"+VIN_SECRET_KEY).encode('utf-8')).hexdigest()[:10]
url = vin_endpoint+"/"+VIN_API_KEY+"/"+controlSum+"/"+ID+".json"
print(url)
json_data = requests.get(url).json()
# print(json_data)

# Convert the data to a pretty-printed JSON format and write it to a text file
with open("balance_output.txt", "w") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
print("Pretty stolen_check_output JSON data has been written to balance_output.txt")

#--------------Compile all data into one text file--------------------------------------
# List of file names to read from
file_names = ['decode_output.txt', 'stolen_check_output.txt', 'vehicle_market_value_output.txt', 'oem_output.txt', 'balance_output.txt']

# Output file where all data will be combined
output_file = 'combined_vehicle_information.txt'
        
# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Loop through each input file
    for file_name in file_names:
        # Write the file name as a header
        outfile.write(f"--- Data from {file_name} ---\n")
        # Open each file in read mode
        with open(file_name, 'r') as infile:
            # Read the content and write it to the output file
            outfile.write(infile.read())
            outfile.write("\n")  # Add a new line between contents of each file (optional)

print(f"All data has been compiled into {output_file}")

