# Generate a techUserToken for further interactions with the MindSphere APIs

The `SetUserToken()` function uses your `client_id` and `client_secret` to get a *techUserToken*. You can find the `SetUserToken()` function in the [auth.py](auth.py) file.

Function structure:
- `SetUserToken(client_id, client_secret) -> str:`

Function inputs:
- `client_id` (string, should be in the form of *hostTenant-appName-appVersion*, e.g. exapleTenant-exampleApp-v0.0.1-1234567)
- `client_secret` (string)

Example output:

![auth.png](doc/auth.png)

> Info: this function was run and tested on python version 3.10.8
