# Generate a techUserToken for further interactions with the MindSphere APIs

The `SetUserToken()` function uses your `client_id` and `client_secret` to get a *techUserToken*. You can find the `SetUserToken()` function in the [auth.py](auth.py) file.

Function structure:
- `SetUserToken(clientID: str, clientSECRET: str) -> str:`

Function inputs:
- `clientID` (string, should be in the form of *hostTenant-appName-appVersion*, e.g. exapleTenant-exampleApp-v0.0.1-1234567)
- `clientSECRET` (string)

> PLEASE NOTE: don't get confused with `userTenant` and `hostTenant`.
> Unless the app, that is granting your credentials (`clientID` & `clientSECRET`) is running on a different tenant than the one you want to access, your `userTenant` = `hostTenant`. Visit the [MindSphere Documentation](https://documentation.mindsphere.io/MindSphere/apis/exchange-tokenmanager/api-tokenmanager-api.html) for more information.

Example output:

![auth.png](doc/auth.png)

> Info: this function was run and tested on python version 3.10.8
