from meraki_sdk.meraki_sdk_client import MerakiSdkClient

X_Cisco_Meraki_API_Key = '15da0c6ffff295f16267f88f98694cf29a86ed87'

MERAKI = MerakiSdkClient(X_Cisco_Meraki_API_Key)

ORGS = MERAKI.organizations.get_organizations()

for ORG in ORGS:
    print("Org ID:  {} and OrgName: {}".format( ORG['id'], ORG['name']))

PARAMS ={}
PARAMS["organization_id"] = "549236"

NETS = MERAKI.networks.get_organization_networks(PARAMS)

for NET in NETS:
    print("Network ID: {0:20s}, Name: {1:45s},Tags: {2:<10s}".format(NET['id'],  NET['name'],  str(NET['tags'])))

Devices = MERAKI.devices.get_network_devices("L_646829496481105433")

for DEVICE in Devices:
    print("Device Model: {0:9s}, Serial:{1:14}, MAC:{2:17}, Firmware: {3:12s}".format(DEVICE['model'], DEVICE['serial'] , DEVICE['mac'], DEVICE['firmware']))
