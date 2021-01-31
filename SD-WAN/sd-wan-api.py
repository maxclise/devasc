import requests

def main():
    api_path = "https://sandbox-sdwan-1.cisco.com"
    requests.packages.urllib3.disable_warnings()
    login_creds = {"j_username": "devnetuser", "j_password": "RG!_Yw919_83"}
    sess = requests.session()
    auth_resp = sess.post(
        f"{api_path}/j_security_check", data=login_creds, verify=False
    )
    device_resp = sess.get(f"{api_path}/dataservice/device", verify=False)
    if device_resp.ok:
        devices = device_resp.json()["data"]

        # Debugging line; pretty-print JSON to see structure
        import json; print(json.dumps(devices, indent=2))

        print(f"Devices managed by DevNet SD-WAN sandbox:")
        for dev in devices:
            print(f"Device IP: {dev['system-ip']:<12} Name: {dev['host-name']}")



if __name__ == '__main__':
    main()