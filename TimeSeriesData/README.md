# Get and store Timeseries Data using MindSphere's Timeseries API

This function uses your [techUserToken](../Authentication/auth.py) to read TimeSeries data from a specified time interval and stores them in a `pd.dataframe` for further data processing. You can find the `timeSeriesData()` function in the [timeSeriesData.py](timeSeriesData.py) file.

Function Inputs:
- `start_date` (string in the form of '%Y-%m-%dT%H:%M:%S.%fZ')
- `end_date` (string in the form of '%Y-%m-%dT%H:%M:%S.%fZ')

> PLEASE NOTE: by default, the `timeSeriesData()` function is accessing the *global variable* `techUserToken`. If don't want to use global variables, you need to pass the `techUserToken` as a third input for the `timeSeriesData()` function.

Example Output:

![example time series data output](doc/timeSeriesData.png)

> Info: this function was run and tested on python version 3.10.8
