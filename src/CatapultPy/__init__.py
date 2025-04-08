import pandas as pd
import numpy as np
import json
import requests


# Create Token Class to have headers and base url
class ofToken:
  def __init__(self, api_token, region):
     self.api_token = api_token
     self.region = region
     self.url_base = "https://connect-" + region + ".catapultsports.com/api/v6/"
     self.headers = {
    "accept": "application/json",
    "authorization": "Bearer " + api_token
    }

# Create Token System
def ofCreateToken(api_key, region = "us"):
    allowed_regions = {"us", "eu", "au", "cn"}
    if region not in allowed_regions:
        raise ValueError(f"Invalid location: {region}")
    
    token = ofToken(api_key, region)
    return(token)

# Activity Function Wrappers
def ofGetActivities(token):
   url = token.url_base + "activities"
   response = requests.get(url, headers=token.headers)
   data = json.loads(response.text)
   df = pd.DataFrame(data)
   return(df)

def ofGetActivitiesAthletes(token, activity_id):
   url = token.url_base + "activities/" + activity_id + "/athletes"
   response = requests.get(url, headers=token.headers)
   data = json.loads(response.text)
   df = pd.DataFrame(data)
   return(df)

def ofGetActivitiesPeriods(token, activity_id):
   url = token.url_base + "activities/" + activity_id + "/periods"
   response = requests.get(url, headers=token.headers)
   data = json.loads(response.text)
   df = pd.DataFrame(data)
   return(df)

def ofGetActivitiesTags(token, activity_id):
   url = token.url_base + "activities/" + activity_id + "/tags"
   response = requests.get(url, headers=token.headers)
   data = json.loads(response.text)
   df = pd.DataFrame(data)
   return(df)

def ofGetActivitiesDevices(token, activity_id):
   url = token.url_base + "activities/" + activity_id + "/devices"
   response = requests.get(url, headers=token.headers)
   data = json.loads(response.text)
   df = pd.DataFrame(data)
   return(df)

# Athletes Wrapper
def ofGetAthletes(token):
   url = token.url_base + "athletes"
   response = requests.get(url, headers=token.headers)
   data = json.loads(response.text)
   df = pd.DataFrame(data)
   return(df)

# Events Wrapper

def ofGetActivityEvents(token, activity_id, athlete_id, events):
    if not isinstance(events, list):
        raise TypeError("events must be a list")
    url = token.url_base +  "activities/" + activity_id + "/athletes/" + athlete_id + "/events?event_types="
    if len(events ) < 1:
       raise ValueError("Must Include at least 1 event")
    elif len(events) == 1:
       url += events[0]
    else:
       for e in events:
          url += e + "%2C"
       url = url[:-3]
    response = requests.get(url, headers=token.headers)
    data = json.loads(response.text)
    df = pd.DataFrame(data)
    return(df)

def ofGetActivityEfforts(token, activity_id, athlete_id, efforts= ['acceleration', 'velocity']):
    if not isinstance(efforts, list):
        raise TypeError("events must be a list")
    url = token.url_base +  "activities/" + activity_id + "/athletes/" + athlete_id + "/efforts?effort_types="
    if len(efforts ) < 1:
       raise ValueError("Must Include at least 1 event")
    elif len(efforts) == 1:
       url += efforts[0]
    else:
       for e in efforts:
          url += e + "%2C"
       url = url[:-3]
    response = requests.get(url, headers=token.headers)
    data = json.loads(response.text)
    df = pd.DataFrame(data)
    return(df)

# Parameters Wrapper
def ofGetParams(token):
   url = token.url_base + "parameters"
   response = requests.get(url, headers=token.headers)
   data = json.loads(response.text)
   df = pd.DataFrame(data)
   return(df)


# Get Stats Groups
# Filters must be a dict with name, compariosn, and values
def ofGetStats(token, params, group_by, filters):
    if not isinstance(group_by, list):
        raise TypeError("group_by must be a list")
    if not isinstance(params, list):
        raise TypeError("parameters must be a list")
    if not isinstance(filters, dict):
        raise TypeError("filters must be a dict")

    url = token.url_base + "stats"

    payload = {
       "filters" : [filters],
       "group_by": group_by,
       "parameters": params
       
    }
    headers = token.headers
    headers['content-type'] = 'application/json'    

    response = requests.post(url, json=payload, headers=headers)

    data = json.loads(response.text)
    df = pd.DataFrame(data)
    return(df)


# Get 10hz Data

def ofGetActivity10hz(token, activity_id, athlete_id):
    url = token.url_base + "activities/" + activity_id + "/athletes/" + athlete_id+ "/sensor"
    response = requests.get(url, headers=token.headers)
    data = json.loads(response.text)
    df = pd.DataFrame(data)
    return(df)



