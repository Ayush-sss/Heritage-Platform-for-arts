from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Define endpoint to retrieve information about an artwork by its ID
@app.route('/artwork/<int:artwork_id>', methods=['GET'])
def get_artwork(artwork_id):
    # Retrieve HTML page for artwork from India Art Heritage website
    url = f'http://www.indiaartheritage.info/Scripts/artifactdescription.asp?ArtifactID={artwork_id}'
    response = requests.get(url)
    
    # Parse HTML page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract information about artwork from parsed HTML
    title = soup.find('span', {'id': 'lblTitle'}).text.strip()
    artist = soup.find('span', {'id': 'lblArtistName'}).text.strip()
    category = soup.find('span', {'id': 'lblCategory'}).text.strip()
    period = soup.find('span', {'id': 'lblPeriod'}).text.strip()
    description = soup.find('span', {'id': 'lblDescr'}).text.strip()
    
    # Return artwork information as JSON
    artwork = {'id': artwork_id, 'title': title, 'artist': artist, 'category': category, 'period': period, 'description': description}
    return jsonify(artwork)

if __name__ == '__main__':
    app.run()
