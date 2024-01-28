# crt.sh Subdomain Fetcher

This Python script is designed to interact with **crt.sh** to retrieve a list of subdomains associated with a specified main domain. This tool is particularly useful for cybersecurity professionals and researchers who need to conduct domain reconnaissance.

## Features

- **Domain Querying**: Input a main domain to find its subdomains.
- **crt.sh Integration**: Leverages crt.sh, a popular SSL/TLS certificate search tool.
- **Custom Output File**: Optionally specify an output file to save the results.

## Requirements

- Python 3
- `requests` library: Install using `pip install requests`
- `bs4` (BeautifulSoup) library: Install using `pip install beautifulsoup4`

## Usage

1. **Clone the Repository**: First, clone or download this repository to your local machine.
2. **Install Dependencies**: Ensure Python 3 is installed. Then, install the required Python packages (`requests` and `beautifulsoup4`).
3. **Running the Script**:
   - Execute the script using the command:
     ```
     python crtsh_subdomain_fetcher.py --domain yourdomain.com
     ```
   - Optionally, specify an output file:
     ```
     python crtsh_subdomain_fetcher.py --domain yourdomain.com --outputfile path/to/output.txt
     ```

## Script Parameters

- `--domain`: (Required) The main domain for which to find subdomains.
- `--outputfile`: (Optional) File path to save the list of found subdomains.

## How It Works

The script makes an HTTP GET request to crt.sh with the specified domain. It then parses the HTML response to extract a list of subdomains. This list can be printed to the console or saved to an output file.

## Limitations and Disclaimer

- The accuracy of the results depends on the data available on crt.sh.
- This tool should be used ethically and legally.

## Contributions

Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is open-source and is licensed under the MIT License - see the LICENSE file for details.

---

**Note**: This script is provided "as is", with no warranty of any kind. Use at your own risk.

## Credits

This script is based on the original work found in [this gist](https://gist.github.com/manasmbellani/4b4d13a2b630ea2c57fba491a079a4fc) by Manas Bellani.