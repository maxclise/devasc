import requests
import json


def main():
    #  API Base URL
    url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
    payload = None

    token_headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
        "Accept": "application/json"
    }
    response = requests.request('POST', url, headers=token_headers, data=payload)
    response = response.text.encode('UTF-8')
    data = json.loads(response)
    for k,v in data.items():
        token = v

    device_url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'

    device_headers ={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Auth-Token": str(token)
    }
    response = requests.request("GET", device_url, headers=device_headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    main()