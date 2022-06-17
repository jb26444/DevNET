import requests
import json
import re
import csv
import yaml
import os
import logging
import argparse
import textwrap

# logging_format = "[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S]"
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s - %(message)s')

logger = logging.getLogger(__name__)

SECURE_CONN = False  # whether to use HTTPS, SSL certificate needed, not supported for now (TODO)
API_TOKEN = '80c0b7e09101514c51f9a1ddc87d29c'  # token for IP Fabric API access
api_url = 'https://ipfabric.cz.prod/api/v1/tables/addressing/managed-devs'  # IP Fabric API server endppoint
SNAPSHOT_ID = '$last'  # snapshot ID, $last is a symbolic tag for the last snapshot made


def requestData(api_url, api_token, secured, request_payload):
    """Request data from IPF's API endpoint.
        api_url : string
            URL to send the request to
        api_token : UUID string
            api token to access IP Fabric's data
        secured : boolean
            if IPF server has valid certificate then the secured should be True
        request_payload : JSON object
            infomration about columns and snapshot ID
        return: api_response {'data': [], '_meta': {}}
    """
    request_headers = {'X-API-Token': api_token, 'Content-Type': 'application/json'}
    try:
        api_response = requests.post(api_url, headers=request_headers, json=request_payload, verify=SECURE_CONN)
    except requests.exceptions.SSLError as ssl_err:
        logger.info('\n  ERROR - Unable verify SSL certificate for {}'.format(api_url))
        logger.info('  -- MESSAGE: ', ssl_err)
    if not api_response.ok:
        logger.info('  API POST Error - Unable to POST data from endpoint: {}'.format(api_url))
        logger.info('  -- MESSAGE: ', api_response.text)
        return {}
    logger.info(f"Successfully fetched data from API endpoint - '{api_url}'")
    return api_response.json()

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
    "siteName": [
      "like",
      "HCI"
    ],
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

def main():
    requestData()

if __name__ == "__main__":
    main()


