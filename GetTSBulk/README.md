# Get and store over 2000 Datapoints using MindSpheres Timeseries Bulk API

This function uses your [techUserToken](./Authentication/auth.py) to read Timeseries data from a specified time interval and stores them in a `pd.dataframe` for further data processing. You can find the `timeSeriesBulk()` function in the [timeSeriesBulk.py](timeSeriesBulk.py) file. You can use the Timeseries Bulk API if you want to retreive more than 2000 datapoints in a single API call.

Function structure:
- `timeSeriesBulk(start_date : str, end_date : str) -> pd.dataframe:`

Function inputs:
- `start_date` (string in the form of '%Y-%m-%dT%H:%M:%S.%fZ')
- `end_date` (string in the form of '%Y-%m-%dT%H:%M:%S.%fZ')

> PLEASE NOTE: by default, the `timeSeriesBulk()` function is accessing the *global variable* `techUserToken`. If you don't want to use global variables, you need to pass the `techUserToken` as a third input for the `timeSeriesBulk()` function.

> The `timeSeriesBulk()` function is using the helper function `ToDateObject()`. This usage is fully optional, but converting the dataframe timestamps from `str` to `datetime.datetime` is needed for many further steps like plotting, calculation and analysis...

Example Output:

[Example Bulk Output](/doc/timeSeriesBulk.png)

> Info: this function was run and tested on python version 3.10.8


