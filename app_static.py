# app_static.py

from flask import Flask, render_template, request
import os

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'umls_extracted_terms.txt')

def load_static_keywords():
    with open(DATA_PATH, 'r') as f:
        keywords = [line.strip().lower() for line in f if line.strip()]
    return keywords

def extract_static_keywords(text, keywords):
    text_lower = text.lower()
    found = []
    for kw in keywords:
        if kw in text_lower:
            found.append(kw)
    return found

@app.route('/', methods=['GET', 'POST'])
def index():
    keywords = load_static_keywords()
    results = []
    if request.method == 'POST':
        input_text = request.form.get('text', '')
        results = extract_static_keywords(input_text, keywords)
    else:
        input_text = ''
    return render_template('index.html', input_text=input_text, results=results, mode='Static')

if __name__ == '__main__':
    app.run(debug=True)
