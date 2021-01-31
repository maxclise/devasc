import requests

def main():
    #  API Base URL
    url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
    payload = None

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
        "Accept": "application/json"
    }
    response = requests.request('POST', url, headers=headers, data=payload)
    print(response.text.encode('utf8'))


if __name__ == '__main__':
    main()