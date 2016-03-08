
from pyzabbix import ZabbixAPI
import sys, json

if len(sys.argv) > 1:
    ZABBIX_SERVER = sys.argv[1]
else:
    ZABBIX_SERVER = 'http://localhost'


zapi = ZabbixAPI(ZABBIX_SERVER)

zapi.login('admin', 'zabbix')

actions = zapi.template.get(filter={"name": "Restcomm Cluster Template"})

print json.dumps(actions)