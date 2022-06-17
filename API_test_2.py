import requests
import logging
import json

# logging_format = "[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S]"
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s - %(message)s')


url = "https://ipfabric.cz.prod/api/v1/tables/addressing/managed-devs"
api_key = "80c0b7e09101514c51f9a1ddc87d29c"

header = {"Authorization": "YES", "Content-Type": "application/json"}

payload = {
  "columns": [
    "id",
    "sn",
    "hostname",
    "intName",
    "stateL1",
    "stateL2",
    "siteKey",
    "siteName",
    "dnsName",
    "dnsHostnameMatch",
    "vlanId",
    "dnsReverseMatch",
    "mac",
    "ip",
    "net",
    "type",
    "vrf"
  ],
  "filters": {
    "ip": [
      "color",
      "eq",
      "30"
    ]
  },
  "pagination": {
    "limit": 500,
    "start": 0
  },
  "snapshot": "2f8e228b-8bd8-4763-98c4-f83aae819ada",
  "reports": "/technology/addressing/managed-ip"
}

getdata = requests.get(url, auth=api_key, headers=header, verify=False,)

response = getdata.json()
print(response)