import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
image = Image.open('ajaxbanner.jpeg')


# Display title and text
st.title("Week 1 - Data and Visualization")
st.write("Finding the closest/cheapest AirBnB venues to the Johan Cruijff ArenA")
st.image(image, caption='Ajax Arena Ultra Banner')
st.markdown("Here we can see the dataframe created during this weeks project.")

# Read dataframe
dataframe = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Meters from chosen location",
        "Location",
    ],
)

# We have a limited budget, therefore we would like to exclude
# listings with a price above 100 pounds per night
dataframe = dataframe[dataframe["Price"] <= 100]

# Display as integer
dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
# Round of values
dataframe["Price"] = "£ " + dataframe["Price"].round(2).astype(str) 
# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "Johan Cruijff ArenA", 0.0: "Airbnb listing"}
)

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("Below is a map showing all the Airbnb listings with a red dot and the Johan Cruijff ArenA with a blue dot.")

# Create the plotly express figure
fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    zoom=10,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Meters from chosen location", "Location"],
    labels={"color": "Locations"},
)
fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Show the figure
st.plotly_chart(fig, use_container_width=True)
