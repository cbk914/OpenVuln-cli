# OpenVuln API cli
# Author: cbk914
# OpenVuln API cli
# Author: cbk914
import argparse
import requests
import json
from json_schema import validate
import sys

if sys.version_info[0] >= 3:
    unicode = str

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

try:
    response = requests.post(auth_url, headers=headers, json=payload)
    # Extract the authentication token from the response
    token = response.json()["token"]
    # Add the token to the headers for future requests
    headers["Authorization"] = "Bearer " + token
    # Check if the request was successful
    if response.status_code != 200:
        print('Error: Failed to authenticate with Cisco PSIRT OpenVuln API')
        exit(1)
except Exception as e:
    print("Error: Failed to authenticate with Cisco PSIRT OpenVuln API")
    print("Error details:", e)
    exit(1)
    
   
# Search for vulnerabilities by name or CVE
if args.search:
    search_url = "https://api.cisco.com/security/advisories/psirt-openvuln/vuln-search"
    search_payload = {
        "search": args.search
    }
    try:
        search_response = requests.post(search_url, headers=headers, json=search_payload)
        # check if request was successful
        if search_response.status_code != 200:
            print("Error: Failed to search for vulnerabilities")
            exit(1)
        else:
            print(search_response.json())
    except Exception as e:
        print("Error: Failed to search for vulnerabilities")
        print("Error details:", e)
        exit(1)   

# Retrieve vulnerability details
if args.vuln:
    vuln_url = f"https://api.cisco.com/security/advisories/psirt-openvuln/vuln/{args.vuln}"
    try:
        response = requests.get(vuln_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        exit(1)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        exit(1)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        exit(1)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong",err)
        exit(1)
    data = json.loads(response.text)
    if response.status_code != 200:
        print('Error: Failed to retrieve vulnerability information')
        exit(1)        

# Descargar el esquema de validación desde la API de Cisco PSIRT OpenVuln
schema_url = "https://api.cisco.com/security/advisories/psirt-openvuln/v1/schema"
response = requests.get(schema_url)
schema = json.loads(response.text)

# Validar la estructura de los datos JSON antes de cargarlos
try:
    validate(data, schema)
    print("JSON data structure is valid.")
except json_schema.exceptions.ValidationError as e:
    print("JSON data structure is not valid.:", e)
    exit(1)    

# Parse JSON response
data = json.loads(response.text)

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
        json.dump(data, f)
        print(f"Vulnerability details exported to {args.output}")
