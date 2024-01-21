# Done
import requests
import pdfkit
from bs4 import BeautifulSoup
import re
def virustotal_scan(api_key, url):
    # Submit the URL for scanning
    params = {'apikey': api_key, 'resource': url}
    scan_url = 'https://www.virustotal.com/vtapi/v2/url/report'
    response = requests.get(scan_url, params=params)
    scan_result = response.json()

    # Check if the scan was successful
    if scan_result['response_code'] != 1:
        print(f"Error: {scan_result['verbose_msg']}")
        return

    # Format scan results into HTML
    html_result = f"""
    <html>
    <head>
        <title>VirusTotal Scan Report for {url}</title>
    </head>
   
    <body style="background-color:white;">
        <h1>VirusTotal Scan Report for {url}</h1>
        <p><strong>URL:</strong> {url}</p>
        <p><strong>Scan ID:</strong> {scan_result['scan_id']}</p>
        <p><strong>Scan Date:</strong> {scan_result['scan_date']}</p>
        <p><strong>Positives:</strong> {scan_result['positives']}</p>
        <p><strong>Total:</strong> {scan_result['total']}</p>
        <h2>Scan Results:</h2>
        <ol>
    """

    for scan_engine, result in scan_result['scans'].items():
        html_result += f"<li><strong>{scan_engine}:</strong> {result['result']}</li>"

    html_result += """
        </ol>
    </body>
    </html>
    """

    # Save the HTML report to a file
    html_file_path = f'report.html'
    with open(html_file_path, 'w') as html_file:
        html_file.write(html_result)

    print(f"HTML Report saved at: {html_file_path}")
def pdf():
    with open('report.html') as f:
        pdfkit.from_file(f, 'out.pdf')
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual VirusTotal API key
    api_key = '57e3de8428a9e14885e553719f4800e738d2150b1058e51ee9b1dc0b9b0a044d'

    # Replace 'https://example.com' with the URL you want to scan
    url_to_scan = 'https://youtube.com'

    virustotal_scan(api_key, url_to_scan)
    pdf()
