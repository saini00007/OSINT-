# done
import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error accessing the webpage: {e}")
        return None

def analyze_content(html_content):
    if not html_content:
        return None

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract information from the parsed HTML
    title = soup.title.text.strip() if soup.title else 'N/A'
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_description['content'].strip() if meta_description else 'N/A'

    # Extract links
    links = [link['href'] for link in soup.find_all('a', href=True)]

    # Extract paragraphs
    paragraphs = [p.text.strip() for p in soup.find_all('p')]

    # Extract images
    images = [img['src'] for img in soup.find_all('img', src=True)]

    return {
        'title': title,
        'meta_description': meta_description,
        'links': links,
        'paragraphs': paragraphs,
        'images': images
    }

if __name__ == "__main__":
    url = "https://www.google.com"  # Replace with the desired URL

    html_content = get_html_content(url)
    if html_content:
        analysis_result = analyze_content(html_content)
        print("\nContent Analysis:")
        for key, value in analysis_result.items():
            print(f"{key.capitalize()}: {value}")
