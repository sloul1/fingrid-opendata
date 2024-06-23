########### Python 3.2 #############
import urllib.request, json, os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()


# Read API key from .env file
api_key = os.getenv('API_KEY')
if api_key is None:
    raise Exception("Failed to load API key from .env file")

## Create test for API key validation?

# Test if Fingrid API is active before making further data queries.
try:
    url = "https://data.fingrid.fi/api/notifications/active"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'x-api-key': api_key,
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        print("Fingrid API is active.")
    else:
        raise Exception(f"Unexpected status code: {response.getcode()}")
except Exception as e:
    print(f"Error when checking API availability: {e}")
    exit() # Exit if the API is not available

# Get user input for parameters
print("Available dataset IDs are listed in https://data.fingrid.fi/en/datasets")
dataset_id = input("Enter dataset ID: ")
start_time = input("Enter start time (format: YYYY-MM-DDTHH:MM:SSZ): ")
end_time = input("Enter end time (format: YYYY-MM-DDTHH:MM:SSZ): ")
format_ = input("Enter desired output format (json = default, csv or xml): ")
one_row_per_time_period = input("Do you want one row per time period? (yes/no): ")
page_size = int(input("How many results per page?: "))
locale = input("Enter locale (en/fi): ")
sort_by = input("Enter sort by (startTime/endtime): ")
sort_order = input("Enter sort order (asc/desc): ")

try:

    # Construct the URL with user input
    url = "https://data.fingrid.fi/api/data?format=" + format_ + "&locale=" + locale + "&datasets="+ dataset_id + "&startTime=" + start_time + "&endTime=" + end_time + "&oneRowPerTimePeriod=" + ("true" if one_row_per_time_period.lower() == "yes" else "false") + "&page=1&pageSize=" + str(page_size) + "&sortBy=" + sort_by + "&sortOrder=" + sort_order
    
    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'x-api-key': api_key,
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    
    # Define filetype according fo format

    output_format = format_.lower()
    if output_format == 'csv':
        file_name = 'output.csv'
        file_extension = '.csv'
    # xml can't use one_row_per_time_period option???     
    elif output_format == 'xml':
        file_name = 'output.xml'
        file_extension = '.xml'
    else:
        file_name = 'output.json'
        file_extension = '.json'
    
    # Save the JSON file from API query
    
    with open(file_name, 'w') as f:
        f.write(response.read().decode('utf-8'))

    print(response.getcode())
    if response.getcode() == 200:
        print(f'''API request successful. Wrote to file "{file_name}"''')
    # print(response.read())
except Exception as e:
    print(e)
####################################