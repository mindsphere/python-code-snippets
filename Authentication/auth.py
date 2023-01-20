# function SetUserToken takes client_id and client_secret as input and returns the techUserToken.
# techUserToken can be used to authenticate against the MindSphere API, e.g. to request TimeSeries Data

#Prerequisites:
import base64
import requests
import json
gateway = 'https://gateway.eu1.mindsphere.io'
technicalTokenMgmtAPI = '/api/technicaltokenmanager/v3'

def SetUserToken(id: str, secret: str) -> str:
    ServiceUrl = gateway + technicalTokenMgmtAPI + '/oauth/token'
    decode = id+":"+secret
    decode = decode.encode('UTF-8')
    encode = base64.b64encode(decode)
    str_encode = encode.decode('UTF-8')
    key = "Bearer "+ str_encode
    headers = {'X-SPACE-AUTH-KEY': key, 'Content-Type': 'application/json'}
    payload = json.dumps({
        "grant_type": "client_credentials",
        "appName": clientID.split("-")[1],
        "appVersion": clientID.split("-")[2],
        "hostTenant": clientID.split("-")[0],
        "userTenant": userTenant
    })
    r = requests.request("POST", url=ServiceUrl, headers=headers, data=payload)
    if r.status_code == 200:
        response_encoded = r.content
        response = response_encoded.decode('UTF-8')
        json_response = json.loads(response)
        token = json_response['access_token']
        global techUserToken
        # techUserToken = token <- OPTIONAL: if the function should set the techUserToken as global variable
        print(f'[{r.status_code}] - saved techUserToken')
        return techUserToken
    else:
        print(f'[{r.status_code}] - Error retreiving techUserToken')
        raise ValueError
  
