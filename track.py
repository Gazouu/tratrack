import requests
import json

def get_ip_data(ip, api_key):
    base_url = "https://www.ipqualityscore.com/api/json/ip/"
    params = {
        "strictness": 1,
        "fast": "false",
        "user_agent": "false",
        "mobile": "false",
        "proxy": "true",
        "vpn": "false",
        "asn": "false",
        "org": "false",
        "carrier": "false",
        "public_proxy": "true",
        "private_proxy": "false",
        "infrastructure": "false",
        "residential": "false",
        "node": "false",
        "tor": "false",
        "active": "true",
        "continent": "false",
        "country": "false",
        "region": "false",
        "city": "false",
        "isp": "false",
        "time_zone": "false",
        "lat": "false",
        "long": "false",
        "accuracy": "false"
    }
    
    response = requests.get(base_url + api_key + '/' + ip, params=params)
    data = response.json()

    return data

api_key = "19fGirhqx6lSuh6frRLDVF8s2MpV0VW6"

ip_address = input("Entrer Adresse IP : ")

ip_data = get_ip_data(ip_address, api_key)

print("Information collecter {}:".format(ip_address))
print(json.dumps(ip_data, indent=2))
