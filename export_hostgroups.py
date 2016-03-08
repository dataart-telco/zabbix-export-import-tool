
from pyzabbix import ZabbixAPI
import sys, json

if len(sys.argv) > 1:
    ZABBIX_SERVER = sys.argv[1]
else:
    ZABBIX_SERVER = 'http://localhost'


zapi = ZabbixAPI(ZABBIX_SERVER)

zapi.login('admin', 'zabbix')

actions = zapi.hostgroup.get(
    output="extend",
    filter={"name": "Restcomm Cluster"})

print json.dumps(actions)