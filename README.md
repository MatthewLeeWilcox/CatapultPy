# CatapultPy 

A lightweight Python wrapper for the Catapult Sports OpenField API. This package is modeled after `CatapultR` and is designed to make it easier to pull data into Python for analysis.

---

## Table of Contents

- [Installation](#installation)
- [Basic Functions](#basic-functions)
- [Activity-Based Functions](#activity-based-functions)
- [Aggregated Data](#aggregated-data)
- [10Hz Data](#10hz-data)

---

## Installation

Install via pip:

```
pip install CatapultPy
```

## Basic Functions

### 

```
token = ofCreateToken(api_key, region = "us")
```
Creates the token to call the API. Must include your region name being "us", "eu", "au", "cn".

```
ofGetActivities(token)
```
Returns a pandas dataframe of all of the activities.

```
ofGetAthletes(token)
```
Get a Pandas Dataframe of all the athletes within a dataframe. 

```
ofGetParams(token)
```
Return a Pandas Dataframe of all paramaters.

### Activity based Functions

```
ofGetActivitiesAthletes(token, activity_id)
```
Returns a Pandas dataframe of all the Athletes from within a activity. Must input the activity id.

```
ofGetActivitesPeriod(token, activity_id)
```
Return a Pandas dataframe of all the periods within an activity.

```
ofGetActivitiesTags(token, activity_id)
```
Return a Pandas dataframe of all the tags within a activity.

```
ofGetActivitiesDevices(token, acitvity_id)
```
Return a Pandas Dataframe of all the devices within a activity.

```
ofGetActivityEvents(token, activity_id, athlete_id, events = ["ima_jumps", "baseball_swing"])
```
Return a Pandas Dataframe of all the events for a single athlete in a activity. events must be listed in a list format.

```
ofGetActivityEfforts(token, activity_id, athlete_id, efforts= ['acceleration', 'velocity'])
```
Return a Pandas Dataframe of all the efforts for a single athlete in a activity. Effort can be acceleartion, velocity or both. It is defaulted as both.

### Aggragated data

```
ofGetStats(token,
            params = ["athlete_name", "date", "start_time", "end_time", "position_name", 
                    "total_distance", "total_duration", "total_player_load", "max_vel", 
                    "hsr_efforts", "max_heart_rate", "mean_heart_rate", 
                    "period_id", "period_name", "activity_name"],
            group_by = ["athlete", "period", "activity"],
            filters = {
                "name" : "activity_id",
                "comparison" : "=",
                "values" : ["activity_id_1", "activity_id_2"]
            })
```

Returns a Pandas Dataframe of aggragated stats. params and group_by must be inputed as lists. Filters must be imputed as a dicitonary, values must be implemented as a list of activity_id's.

### 10Hz Data

```
ofGetActivity10hz(token, activity_id, athlete_id)
```

Returns a Pandas Dataframe of 10 Hz data of an athlete from within an activity.


