# OpenVuln API cli
# Author: cbk914
import argparse
import requests
import json

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--vuln", help="Vulnerability ID")
parser.add_argument("-o", "--output", help="Output file")
parser.add_argument("-u", "--username", required=True, help="Cisco PSIRT OpenVuln API username")
parser.add_argument("-api", "--apikey", required=True,help="Cisco PSIRT OpenVuln API key")
parser.add_argument("-s", "--search", help="Search term (name or CVE)")
args = parser.parse_args()

# Authenticate with Cisco PSIRT OpenVuln API
auth_url = "https://api.cisco.com/security/advisories/psirt-openvuln/authenticate"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
payload = {
    "username": args.username,
    "apikey": args.apikey
}
response = requests.post(auth_url, headers=headers, json=payload)

# Extract the authentication token from the response
token = response.json()["token"]

# Add the token to the headers for future requests
headers["Authorization"] = "Bearer " + token

# Check if the request was successful
if response.status_code != 200:
    print('Error: Failed to retrieve vulnerability information')
    exit(1)
    
# Search for vulnerabilities by name or CVE
if args.search:
    search_url = "https://api.cisco.com/security/advisories/psirt-openvuln/vuln-search"
    # endpoint = "https://api.cisco.com/security/advisories/psirt-openvuln-api/v1"
    search_payload = {
        "search": args.search
    }
    search_response = requests.post(search_url, headers=headers, json=search_payload)
    print(search_response.json())    

# Parse JSON response
vuln_info = json.loads(response.text)

# Print vulnerability information to console
print("ID:", data['id'])
print("Advisory ID:", data['advisoryId'])
print("CVSS Base Score:", data['cvssBaseScore'])
print("CVSS Temporal Score:", data['cvssTemporalScore'])
print("CVSS Vector:", data['cvssVector'])
print("CWE ID:", data['cweId'])
print("Description:", data['description'])
print("Publish Date:", data['publishDate'])
print("Software Versions:", data['softwareVersions'])
print("Threat Category:", data['threatCategory'])
print("Title:", data['title'])

# Export the vulnerability details to a file
if args.output:
    with open(args.output, "w") as f:
        json.dump(vuln_info, f)
        print(f"Vulnerability details exported to {args.output}")
