import requests
import json
import os


def main():
    api_path = "https://api.meraki.com/api/v1"
    headers = {
        "Content": "application/json",
        "X-Cisco-Meraki-API-Key": "44774a7665649869244716410fe7975e99d2c072",
    }
    requests.packages.urllib3.disable_warnings()

    sess = requests.session()
    get_org = sess.get(f'{api_path}/organizations', data=headers, verify=False)
    get_org = get_org.text.encode('UTF-8')
    #  print(json.loads(str(get_org)))
    print(get_org)

if __name__ == '__main__':
    main()