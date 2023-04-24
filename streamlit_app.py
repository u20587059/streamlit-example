from collections import namedtuple
import altair as alt
import math
import pandas as pd
import geopandas as gpd 
from shapely.geometry import Point
import streamlit as st

st.write("TravelWorld.com")
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

minAir = airports['Number of airports'].min()
minAir

output
latitude = airports['latitude']
longitude = airports['longitude']
airport_locations = pd.DataFrame(latitude).join(longitude)
airport_locations

st.map(airport_locations)



