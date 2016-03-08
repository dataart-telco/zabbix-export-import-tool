
from pyzabbix import ZabbixAPI
import sys, json, os

if len(sys.argv) > 2:
    IMPORT_DIR = sys.argv[1]
    ZABBIX_SERVER = sys.argv[2]
else:
    IMPORT_DIR = "import_pack"
    ZABBIX_SERVER = 'http://localhost'

print "*****"
print "** App iports files in Lexicographical order from '{0}' folder".format(IMPORT_DIR)
print "*****"
print ""

zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('admin', 'zabbix')

for f in os.listdir(IMPORT_DIR):
    data = readFile(f)
    if "action" in f.basename():
        importAction(data)
    if "hostgroup" in f.basename():
        importHostGroups(data)
    if "template" in  f.basename():
        importTemplate(data)
    if "template.xml" in  f.basename():
        importTemplateXml(data)

def readFile(f):
    with open('filename', 'r') as f:
        return f.read()

def importAction( data ):
    zapi.action.create(data)

def importHostGroups( data ):
    zapi.hostgroup.create(data)

def importTemplate( data ):
    zapi.template.create(data)

def importTemplateXml( template ):
    rules = {
        'applications': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'discoveryRules': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'graphs': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'groups': {
            'createMissing': 'true'
        },
        'hosts': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'images': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'items': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'maps': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'screens': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'templateLinkage': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'templates': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'templateScreens': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
        'triggers': {
            'createMissing': 'true',
            'updateExisting': 'true'
        },
    }
    zapi.confimport('xml', template, rules)
