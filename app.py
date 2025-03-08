import os
from google.cloud import bigquery
import folium
from streamlit_folium import st_folium
import streamlit as st
from map_markers import mapping

client = bigquery.Client()

# Streamlit UI
st.title("Find Neighboring States")

# User input
state_name = st.text_input("Enter your state (full name, e.g., 'Texas'):")

def format_state_name_correctly(state):
    first_letter = state[0].upper()
    rest_of_name = state[1:].lower()

    return first_letter + rest_of_name

# Query function, took inspiration from: https://cloud.google.com/python/docs/reference/bigquery/latest
# Used LLM to debug: https://chatgpt.com/share/67cbc4ef-96b0-8003-911c-c40d32730996

def get_neighboring_states(state):
    query = f"""
    SELECT neighbors_state
    FROM `bigquery-public-data.geo_us_boundaries.adjacent_states`
    WHERE state_name = @state
    """

    # Used LLM assistance here, since didn't know how to handle parameters in a query
    job_config = bigquery.QueryJobConfig(
    query_parameters=[
        bigquery.ScalarQueryParameter("state", "STRING", state),
    ]
    )

    query_job = client.query(query, job_config=job_config)
    results = query_job.result()

    # Extract the list of neighbors properly
    neighbors = []
    for row in results:
        neighbors.extend(row["neighbors_state"])  # Since it's a list, extend to get a list of neighbors

    return neighbors

if state_name:
    state_name  = format_state_name_correctly(state_name) # Handle case sensitivity
    try: # Handle crashes
        neighbors = get_neighboring_states(format_state_name_correctly(state_name))
        if neighbors:
            st.write(f"Neighboring states of {state_name}: {', '.join(neighbors)}")
            mapping(state_name,neighbors)
        else:
            st.write(f"No neighboring states found for {state_name}. Check spelling.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
