import requests
import get_mitm_properties

mitm_host=get_mitm_properties.get_mitm_host()
mitm_port=get_mitm_properties.get_mitm_port()

URL = f'http://{mitm_host}:{mitm_port}'
headers = { "shutdown" : "shutdown"}
r = requests.get(url = URL,headers=headers)
