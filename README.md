# OpenVuln-cli

Interface to the OpenVuln API.

**In order to use this script, you will need to have a valid Cisco PSIRT OpenVuln API username and API key.**

is a command line interface (CLI) for the Cisco PSIRT OpenVuln API. It allows you to search for vulnerabilities by name or CVE, authenticate with the API, and retrieve vulnerability details. It also validates the data structure of the response and prints the vulnerability information to the console or exports it to a file.

To use the Cisco PSIRT OpenVuln API console interface in Python, follow these steps:

1. Make sure you have a valid Cisco account and API key. You will need to sign up for an account if you do not have one.
2. Install the necessary libraries by running "pip install requests" in your command line.
3. Download the script and run it with Python.
4. Use the -v or --vuln option to input the vulnerability ID that you want to look up. For example: "python openvuln-cli.py -v cisco-sa-20180829-asr1k"
5. Use the -o or --output option to export the results to a .txt file. For example: "python openvuln-cli.py -v cisco-sa-20180829-asr1k -o results.txt"
6. Use the -u or --user option to input your Cisco account username. For example: "python openvuln-cli.py -v cisco-sa-20180829-asr1k -o results.txt -u my_username"
7. Use the -api or --api_key option to input your Cisco account API key. For example: "python openvuln-cli.py -v cisco-sa-20180829-asr1k -o results.txt -u my_username -api my_API_key"
8. The script will use the provided credentials to authenticate with the Cisco PSIRT OpenVuln API and retrieve information about the specified vulnerability. The results will be printed to the console and, if specified, written to the specified .txt file.

Note: Be sure to keep your Cisco account and API key private, and never share them with others.

Note: This script is using requests, argparse and json librares, please make sure you have them installed.

Note: Unofficial software. I have no relation with Cisco or its partners.
