# fingrid-opendata

Source Fingrid / data.fingrid.fi, license CC 4.0 BY

Further information on Fingrid's open data license and terms of use can be checked at their website's about section.
https://data.fingrid.fi/en/about

"Fingrid is Finland’s transmission system operator."

https://www.fingrid.fi/en/

This program is for retrieving data through Fingrid's open REST API interface. Get your own API key from instructions below.

API instructions: https://data.fingrid.fi/en/instructions

API key is stored in .env file as: API_KEY=insert_your_api_key_here

At this stage this python program retrieves wind power production real time data from Fingrid open data and prints it.
https://data.fingrid.fi/en/datasets/181  

  

Possible future:

- retrieve hourly prices for electricity once in 24 h and store data
- go through retrieved data
- make calculations 
- determine price wise the most advantageous time to charge e-bike battery
- automate smartplug on/off function with configurable treshold levels for electricity price
- statistics for smartplug electricity usage
- data visualization for electricity prices

