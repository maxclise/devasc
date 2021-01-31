import meraki
import os


def main():
    api_key = os.environ.get('MERAKI_KEY')
    dashboard = meraki.DashboardAPI(api_key)
    response = dashboard.organizations.getOrganizations()
    for x in response:
        if 'Blackbaud' in x['name']:
            bb_id = x['id']
        print(x['name'] + ' id is ' + x['id'])

    devices = dashboard.organizations.getOrganizationDevices(organizationId=bb_id)
    for y in devices:
        print(y['name'] + ' IP is ' + str(y['lanIp']))
    #  print(devices)

if __name__ == '__main__':
    main()
