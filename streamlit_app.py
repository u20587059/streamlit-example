from collections import namedtuple
import altair as alt
import math
import pandas as pd
import geopandas as gpd 
from shapely.geometry import Point
import streamlit as st

st.title("Travel World")
st.write("The following dashboard contains information about airlines and airports from OpenFlight")

col_names = ["Airline ID", "Name","Alias","IATA","ICAO","Callsign","Country","Active Airlines"]
airlines = pd.read_csv('airlines.dat', names = col_names)
groupedAirlines = airlines.groupby("Country")["Active Airlines"].count().reset_index()
st.bar_chart(groupedAirlines, x="Country", y="Active Airlines")
groupedAirlines

airport_col = ['Airport ID', 'Number of airports', 'City', 'Country', 'IATA', 'ICAO', 'latitude','longitude', 'Altitude', 'Time Zone', 'DST', 'Tz db time', 'Type', 'Source']
airports = pd.read_csv('airports.dat', sep =",", names=airport_col)
grouped = airports.groupby('Country')
output= grouped.aggregate({'Number of airports':'count'}).reset_index() 
st.bar_chart(output, x="Country", y="Number of airports")

output2 = pd.DataFrame(output)
output2
minimum = output2['Number of airports'].min()
minn = output2['Number of airports'].idxmin()
minimum
minAir = output2.loc[minimum, 'Country']
minAir
maximum = output2['Number of airports'].max()
maxx = output2['Number of airports'].idxmax()
maxAir = output2.loc[maxx, 'Country']
maxAir
maximum

output
latitude = airports['latitude']
longitude = airports['longitude']
airport_locations = pd.DataFrame(latitude).join(longitude)
airport_locations

st.map(airport_locations)

st.caption("The data for this dashboard was taken from OpenFlights")


