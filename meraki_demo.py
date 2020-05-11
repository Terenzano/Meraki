from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
meraki = MerakiSdkClient(token)

orgs = meraki.organizations.get_organizations()


for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        orgId = org['id']

# pprint(orgId)

params = {}
params['organization_id'] = orgId
networks = meraki.networks.get_organization_networks(params)

# pprint(networks)

for network in networks:
    if network['name'] == 'DevNet Sandbox Always on READ ONLY':
        netId = network['id']

vlans = meraki.vlans.get_network_vlans(netId)

# pprint(vlans)

vlan = vlans[0]
vlan['name'] = 'Terence was HERE'

updated_vlan = {}
updated_vlan['network_id'] = netId
updated_vlan['vlan_id'] = vlan['id']
updated_vlan['update_network_vlan'] = vlan

result = meraki.vlans.update_network_vlan(updated_vlan)

result_vlan = meraki.vlans.get_network_vlans(netId)

pprint(result_vlan)
