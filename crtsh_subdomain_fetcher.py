#!/usr/bin/python3

import subprocess
import shlex
import requests
from bs4 import BeautifulSoup
from sys import exit
from argparse import ArgumentParser, RawTextHelpFormatter

### URL to crt.sh to get all the domains
CRTSH_REQUEST_URL = "https://crt.sh/?q="

### Write local output from a command to this file ###
DEFAULT_OUTPUT_FILE = "/tmp/out10.txt"

### User Agent String for web requests
USER_AGENT_STRING = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/60.0.3112.113 Safari/537.36")

DEFINITION = "Runs crtsh to get the domains for the certificates"

def write_output_to_file(outputfile, output):
    with open(outputfile, "wb+") as f:
        f.write(output.encode("utf-8"))

def make_get_request_via_browser(url, browser=None):
    """ Make request for a URL using existing browser, or create a new browser tab """
    if browser:
        browser.get(url)
    else:
        browser = webdriver.Firefox()
        browser.get(url)

    return browser

def make_get_request(url):
    """ Make Get request to a URL """
    headers = {"User-Agent": USER_AGENT_STRING}
    resp = requests.get(url, headers=headers)
    return resp

def get_url(row):
    td_content = row.findAll("td")[5]
    br_split_urls = td_content.get_text(separator="\n").split("\n")
    return '\n'.join(br_split_urls).encode("utf-8")

def main():
    parser = ArgumentParser(description=DEFINITION)

    ### TO_MODIFY: Define the arguments that script takes
    parser.add_argument("--domain", dest="domain", action="store", required=True)
    parser.add_argument("--outputfile", dest="outputfile", action="store", required=False)

    ### Read the arguments, and update executable locations to config
    args = parser.parse_args()
    config = vars(args)

    ### All output from commands executed are stored here
    output = ""
    
    domain = config["domain"]
    url = CRTSH_REQUEST_URL + "%.{}".format(domain)

    print("[i] Making request to url {} to get all domains".format(url))
    resp = make_get_request(url)
    print("[i] Response length: {}".format(len(resp.text)))

    bs = BeautifulSoup(resp.text, "lxml")
    
    print("[i] Getting results table")
    results_table = None
    try:
        tables = bs.findAll("table")
        results_table = tables[2]
    except Exception as e:
        print("[-] Results table not found.")
        print("[-] Error: {}".format(e))
        exit(1)

    if results_table:
        print("[i] Parsing results table (excluding header row)")
        result_rows = None
        try:
            result_rows = results_table.findAll("tr")
            result_rows = result_rows[1:]
        except Exception as e:
            print("[-] result_rows not found")
            print("[-] Error: {}".format(e))
            exit(1)

        if result_rows:
            print("[i] Parsing url from each table row")
            try:
                all_urls = [get_url(r) for r in result_rows]
                #print(all_urls)
            except Exception as e:
                print("[-] Cannot parse domain")
                print("[-] Error: {}".format(e))
                exit(1)

    print("[+] Number of domains found: {}".format(len(all_urls)))
    output = "\n".join([url.decode('utf-8') for url in all_urls])    

    ### Finally write the output to the specified file, if defined
    if "outputfile" in config and config["outputfile"]:
        write_output_to_file(config["outputfile"], output)
    else:
        print("[+] Domains are: ")
        print(output)

if __name__ == "__main__":
    main()
