import requests

gateway = 'https://gateway.eu1.mindsphere.io'
IoTFileServiceAPI = '/api/iotfile/v3/'
deviceId = 'Your AssetId here'

def PutFile(FileName: str) -> None:
    ServiceURL = gateway + IoTFileServiceAPI + deviceId + '/' + FileName
    datafile = open(FileName,'rb')
    filedata = datafile.read()
    datafile.close()
    response = requests.request('PUT', ServiceURL, headers={'Authorization': 'Bearer ' + techUserToken} , data=filedata)
    if response.status_code == 201:
        print(f'Response [{response.status_code}] - file: {FileName} uploaded to asset.')
        return
    else:
        print(f'Response [{response.status_code}]')
        raise ValueError

