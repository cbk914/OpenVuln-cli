# OpenVuln API cli
# Author: cbk914
import argparse
import requests
import json

# Parse command line arguments
parser = argparse.ArgumentParser(description='Retrieve information from Cisco PSIRT OpenVuln API')
parser.add_argument('-v', '--vuln', required=True, help='Vulnerability ID')
parser.add_argument('-o', '--output', help='Output file')
args = parser.parse_args()

# Cisco PSIRT OpenVuln API endpoint and headers
endpoint = 'https://api.cisco.com/security/advisories/'
headers = {'Accept': 'application/json', 'Authorization': 'Basic YOUR_AUTH_TOKEN'}

# Send GET request to retrieve vulnerability information
response = requests.get(endpoint + args.vuln, headers=headers)

# Check if the request was successful
if response.status_code != 200:
    print('Error: Failed to retrieve vulnerability information')
    exit(1)

# Parse JSON response
vuln_info = json.loads(response.text)

# Print vulnerability information to console
print('Vulnerability ID:', vuln_info['id'])
print('CVSS Score:', vuln_info['cvss'])
print('Title:', vuln_info['title'])
print('Advisory:', vuln_info['advisory'])

# Export the vulnerability details to a file
if args.output:
    with open(args.output, "w") as f:
        json.dump(vuln_info, f)
        print(f"Vulnerability details exported to {args.output}")
