import whois

def get_domain_information(url):
    try:
        domain_info = whois.whois(url)
        
        print("Domain Information:")
        for key, value in domain_info.items():
            print(f"{key} : {value}")

    except whois.parser.PywhoisError as e:
        print(f"Error getting domain information: {e}")
        return None

url = input("Enter URL: ")
get_domain_information(url)
