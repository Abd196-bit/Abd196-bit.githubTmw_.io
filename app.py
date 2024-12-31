from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Sample dataset (replace with real data or scraped content)
sample_data = [
    {"title": "How to use Python", "description": "Learn Python from scratch with easy tutorials."},
    {"title": "Flask for beginners", "description": "Build web apps using Flask."},
    {"title": "Search Engine Implementation", "description": "Learn how to create a search engine."},
    {"title": "Scraping Websites with Python", "description": "Extract web data using BeautifulSoup."},
]

# Route to serve the homepage with the search bar
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the search query and return matching results
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    results = []

    if query:
        # Search in the sample dataset
        for item in sample_data:
            if query in item['title'].lower() or query in item['description'].lower():
                results.append(item)

    return jsonify(results)

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
