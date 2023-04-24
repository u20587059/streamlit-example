from collections import namedtuple
import altair as alt
import math
import pandas as pd
import geopandas as gpd 
from shapely.geometry import Point
import streamlit as st

st.title("Travel World")
st.write("The following dashboard contains information about airlines and airports from OpenFlight")

col_names = ["Airline ID", "Name","Alias","IATA","ICAO","Callsign","Country","Airlines"]
airlines = pd.read_csv('airlines.dat', names = col_names)
groupedAirlines = airlines.groupby("Country")["Airlines"].count().reset_index()
st.bar_chart(groupedAirlines, x="Country", y="Airlines")
groupedAirlines
GroupedAir = pd.DataFrame(groupedAirlines)
most = GroupedAir['Airlines'].max()
most2 = GroupedAir['Airlines'].idxmax()
mostAirline = GroupedAir.loc[most2, 'Country']

st.write("The country with the most amount of airlines is " ,mostAirline, "with", most , " airlines")

st.subheader("number of airports in every country")
airport_col = ['Airport ID', 'Number of airports', 'City', 'Country', 'IATA', 'ICAO', 'latitude','longitude', 'Altitude', 'Time Zone', 'DST', 'Tz db time', 'Type', 'Source']
airports = pd.read_csv('airports.dat', sep =",", names=airport_col)
grouped = airports.groupby('Country')
output= grouped.aggregate({'Number of airports':'count'}).reset_index() 
output
st.bar_chart(output, x="Country", y="Number of airports")


output2 = pd.DataFrame(output)
minimum = output2['Number of airports'].min()
minn = output2['Number of airports'].idxmin()
minAir = output2.loc[minimum, 'Country']
maximum = output2['Number of airports'].max()
maxx = output2['Number of airports'].idxmax()
maxAir = output2.loc[maxx, 'Country']

st.write("The country with the most amount of airports is " ,maxAir, "with", maximum , " airports")


latitude = airports['latitude']
longitude = airports['longitude']
airport_locations = pd.DataFrame(latitude).join(longitude)
st.header("A map displaying all the airports on all seven continents")
st.subheader("coordinates for the locations of all airports")
airport_locations

st.map(airport_locations)

st.caption("The data for this dashboard was taken from OpenFlights")


