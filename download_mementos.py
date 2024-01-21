#  pip install wayback
import wayback
from datetime import datetime

# Create web archive client:
client = wayback.WaybackClient()

# Search for copies of nasa.gov web pages saved before 1999:
for record in client.search('https://chat.openai.com/', to_date=datetime(2024, 1, 1)):
    # Get memento record (web page copy):
    memento = client.get_memento(record)

html_content=memento.text
pdf=output.pdf
pdfkit.from_string(html_content, pdf)

    # Generate the name of the file in which we will save the HTML code of theweb page copy (replace the link to the page with / to - (so that no erroroccurs when saving the file) and add .html extension:
    # fileName=memento.memento_url.replace("/","-")+".html"

    # memento_file = open(fileName, "a")
    
    # Write HTML code of the web page copy to the file:
    # memento_file.write(memento.text)
    
    # memento_file.close()