########### Python 3.2 #############
import urllib.request, json, os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Get API key from .env file
api_key = os.getenv('API_KEY')
if api_key is None:
    raise Exception("Failed to load API key from .env file")

try:
    url = "https://data.fingrid.fi/api/datasets/181/data?format=json&locale=en&sortBy=startTime&sortOrder=asc"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'x-api-key': api_key,
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.getcode())
    print(response.read())
except Exception as e:
    print(e)
####################################