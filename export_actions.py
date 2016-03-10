
from pyzabbix import ZabbixAPI
import sys, json

if len(sys.argv) > 1:
    ZABBIX_SERVER = sys.argv[1]
else:
    ZABBIX_SERVER = 'http://localhost'


zapi = ZabbixAPI(ZABBIX_SERVER)

zapi.login('admin', 'zabbix')

actions = zapi.action.get(
#    filter={"name":"Restcomm Cluster"},
    output="extend", 
    selectOperations="extend",
    selectConditions="extend")

print json.dumps(actions)
