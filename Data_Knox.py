from typing import Collection
from meraki_sdk.meraki_sdk_client  import MerakiSdkClient
import json
from pprint import pprint

token = '15da0c6ffff295f16267f88f98694cf29a86ed87'
meraki = MerakiSdkClient(token)

orgs = meraki.organizations.get_organizations()

for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        orgid = org['id']

Parameter ={}
Parameter['organization_id'] = orgid

networks= meraki.networks.get_organization_networks(Parameter)

for net in networks:
    if net['name'] == 'DevNet Sandbox ALWAYS ON':
        networksId = net['id']

devices = meraki.devices.get_network_devices(networksId)
vlans = meraki.vlans.get_network_vlans(networksId)

pprint(vlans)

for vlan in vlans:
    if vlan['name']  ==  'Default':
        vlan_id = vlan['id']

vlan1 = vlans[0]
vlan1['name'] = 'Nsindiso was here'

collect = {}
collect['network_id'] = networksId
collect['vlan_id'] = vlan_id     
collect['update_network_vlan'] = vlan1

result = meraki.devices.update_network_vlan(collect)

pprint(vlans)