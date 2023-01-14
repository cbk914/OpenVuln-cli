# OpenVuln API cli
# Author: cbk914
import argparse
import requests
import json

# Define the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--vuln", required=True, help="Vulnerability ID")
parser.add_argument("-o", "--output", help="Output file name")
args = parser.parse_args()

# Build the API endpoint URL
url = f"https://api.cisco.com/security/advisories/{args.vuln}"

# Send the GET request
response = requests.get(url)

# Check the response status code
if response.status_code != 200:
    print(f"Error: Failed to get vulnerability details, status code: {response.status_code}")
    exit(1)

# Parse the JSON response
vulnerability = json.loads(response.text)

# Print the vulnerability details
print("Title:", vulnerability["title"])
print("CVSS:", vulnerability["cvss"])
print("CWE:", vulnerability["cwe"])
print("CVSS Vector:", vulnerability["cvss-vector"])
print("Description:", vulnerability["description"])

# Export the vulnerability details to a file
if args.output:
    with open(args.output, "w") as f:
        json.dump(vulnerability, f)
        print(f"Vulnerability details exported to {args.output}")
