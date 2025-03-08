# find-your-neighbors

Streamlit app to find and visualize your neighboring states.

## References

Utilize this references heavily to setup API authenthication and call functionality:

- https://googleapis.dev/python/google-api-core/latest/auth.html
- https://cloud.google.com/python/docs/reference/bigquery/latest

Streamlit-Folium reference to develop map functionality:
- https://folium.streamlit.app/

ChatGPT session to solve questions, debug code and brainstorm ideas for app:
Link to Sessions: https://chatgpt.com/share/67cbc4ef-96b0-8003-911c-c40d32730996, https://chatgpt.com/share/67cbd26a-9afc-8003-8603-bcea8be1c335

## How to run

### Must authenticated to make API calls

For information on how to get authenticated: https://cloud.google.com/python/docs/reference/bigquery/latest

### Must install dependencies
Run in virtual environment:

'''
pip install -r requirements.txt
'''

### Run Streamlit locally

If running from Google Cloud: 

'''
streamlit run app.py --server.enableCORS=false
'''

If running in local environment:
'''
streamlit run app.py
'''
## Features?!

### Get your neighboring states

<img width="794" alt="image" src="https://github.com/user-attachments/assets/d549386f-d2e9-4ede-bfbb-65cfdd84afc2" />

### Case sensitivity doesn't matter
<img width="793" alt="image" src="https://github.com/user-attachments/assets/ae5b6326-26cb-4678-8f53-be297fd6866b" />

### Get a map representation of your state and your neighbors

<img width="830" alt="image" src="https://github.com/user-attachments/assets/2e341933-35a4-48a3-92d8-f483eb0d2863" />



