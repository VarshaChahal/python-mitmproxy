from jproperties import Properties

configs = Properties()
with open('app.properties', 'rb') as config_file:
        configs.load(config_file)
        
def get_mitm_port():
    return configs.get("mitm_port").data

def get_mitm_host():
    return configs.get("mitm_host").data