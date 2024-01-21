import re
import requests

def extract_emails(url):
    # Fetch the webpage content
    response = requests.get(url)
    
    if response.status_code == 200:
        # Use regular expression to find email addresses
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        emails = re.findall(email_pattern, response.text)
        
        return emails
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

# Example usage:
webpage_url = "https://W3SCHOOL.COM"
extracted_emails = extract_emails(webpage_url)

if extracted_emails:
    print("Extracted emails:")
    for email in extracted_emails:
        print(email)
else:
    print("No emails found on the webpage.")
