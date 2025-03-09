# find-your-neighbors
Streamlit app to find and visualize your neighboring states.

## Steps to be able to run

### Make sure you have a gcloud project setup

If not in projet:

'''
gcloud config set project [PROJECT_ID]
'''

### Make sure you are authenticated

Run to authenticate if not:

'''
gcloud auth application-default login
'''

### Run Streamlit app

If you are in a cloud service:

'''
streamlit run app.py --enableCORS=false
'''

If you are running in a local machine:

'''
streamlit run app.py
'''
