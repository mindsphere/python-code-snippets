# Prerequisites:
import datetime
import pandas as pd
import requests
import json
gateway = 'https://gateway.eu1.mindsphere.io'
TSBulkAPI = '/api/iottsbulk/v3/'
deviceId = 'Your AssetID here'
propertySetName = 'Your Aspect Name here'

# Helper function to format MindSpheres str timestamp to a python datetime object:
def ToDateObject(Date_In : str) -> datetime.datetime:
    format_in = '%Y-%m-%dT%H:%M:%S.%fZ'
    try:
        time_obj = datetime.datetime.strptime(Date_In, format_in)
    except ValueError:
        format_error = '%Y-%m-%dT%H:%M:%SZ'
        time_obj = datetime.datetime.strptime(Date_In, format_error)
    return time_obj
  
# Main function:
def timeSeriesBulk(start_date: str, end_date: str) -> pd.DataFrame:
  ServiceUrl = gateway + TSBulkAPI + 'timeseries/' + deviceId + '/' + propertySetName + '?from=' + start_date + '&to=' + end_date
  response = requests.request('GET', ServiceUrl, headers={'Authorization': 'Bearer ' + techUserToken, 'accept':'*/*', 'cache-control':'no-cache', 'Content-Type':'application/json'})
  response_data = json.loads(response.text)
  if response.status_code == 200:
      print (f'[{response.status_code}] - OK: asset data received')
  else:
      print(f'[{response.status_code}] - Error ')
      raise ValueError
  data = json.loads(response.content)
  timeseries_data= pd.DataFrame.from_dict(data['records'])
  timeseries_data['_time'] = timeseries_data['_time'].map(lambda x: ToDateObject(x))
  return timeseries_data
