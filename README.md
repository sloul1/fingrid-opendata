# fingrid-opendata

Source Fingrid / data.fingrid.fi, license CC 4.0 BY

"Fingrid is Finland’s transmission system operator." https://www.fingrid.fi/en/

Further information on Fingrid's open data license and terms of use can be checked at their website's about section. https://data.fingrid.fi/en/about

This program is for retrieving data through Fingrid's open data REST API interface.
You will need to get your own API key using instructions below.

API instructions: https://data.fingrid.fi/en/instructions

API key is stored in .env file as: API_KEY=insert_your_api_key_here

Program reads user's API key. Using unauthorized API key will produce error: "HTTP Error 401: Access Denied".
Then program checks if Fingrid API is active. If not program exits.
If API is active program asks user input for parameters and retrieves data accordingly 
from Fingrid open data and prints response as JSON, csv or xml.

Input parameters:

datasetID (int32) Check available datasets at: https://data.fingrid.fi/en/datasets  
startTime (YYYY-MM-DDTHH:MM:SSZ)  
endTime (YYYY-MM-DDTHH:MM:SSZ)  
format (json, csv or xml)  
oneRowPerTimePeriod (boolean) - xml not supported currently  
pageSize (int32)  
locale (en, fi)  
sortBy (startTime, endTime)  
sortOrder (asc, desc)

Running program in Linux cli: diipa@daapa:~/fingrid-opendata$ python3 app.py

![run app](run-app.png?raw=true "Running app (python3 app.py)")

More information on API details: https://developer-data.fingrid.fi/api-details#api=avoindata-api&operation=GetDatasetData


Possible future:

- retrieve hourly prices for electricity once in 24 h and store data
- go through retrieved data and make calculations to determine price wise
  the most advantageous time to charge e-bike battery
- automate smartplug on/off function with configurable treshold levels for electricity price
- statistics for smartplug electricity usage
- data visualization

