import streamlit as st
import folium
from streamlit_folium import st_folium

from USA_state_coords import state_coords

# Function to add markers
def add_marker(state_name, color,m):
    if state_name in state_coords:
        folium.Marker(state_coords[state_name], tooltip=state_name, icon=folium.Icon(color=color)).add_to(m)

def mapping(selected_state, neighbors):
    # Streamlit UI
   # st.title("US State Neighbor Finder 🌎")

    # Create a folium map centered on the US
    m = folium.Map(location=[37.8, -96], zoom_start=4)

    # Add main state marker
    add_marker(selected_state, "red",m)

    # Add neighboring states
    for neighbor in neighbors:
        add_marker(neighbor, "green",m)

    # Display the map
    st_folium(m, width=700, height=500)
