# CatapultPy 
A basic API wrapper for Catapult Sports Openfield Data. Should be similar to CatapultR. 


## Instalation

```
pip install CatapultPy
```

## Basic Functions

```
ofCreateToken(api_key, region = "us")

```
Creates the token to call the API. Must include your region name being "us", "eu", "au", "cn"

```
ofGetActivities(token)
```
Returns a pandas dataframe of all of the activities


```
ofGetActivitiesAthletes(token, activity_id)
```
Returns a Pandas dataframe of all the Athletes from within a activity. Must input the activity id.


