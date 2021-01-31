'''
DNA Center get devices

Uses Cisco Devnet Sandbox
'''

from dnacentersdk import api


def main():
    #  Create DNAC object
    dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac2.cisco.com",
        username='devnetuser',
        password='Cisco123!'
    )

    devices = dnac.devices.get_device_list()

    for device in devices['response']:
        print(f"ID: {device['id']} IP: {device['managementIpAddress']}")


if __name__ == '__main__':
    main()