from meraki_sdk.meraki_sdk_client import MerakiSdkClient

X_Cisco_Meraki_API_Key = '15da0c6ffff295f16267f88f98694cf29a86ed87'

MERAKI = MerakiSdkClient(X_Cisco_Meraki_API_Key)

ORGS = MERAKI.organizations.get_organizations()

for ORG in ORGS:
    print("Org ID:  {} and OrgName: {}".format( ORG['id'], ORG['name']))