# app_dynamic.py

from flask import Flask, render_template, request
import spacy
import scispacy
from scispacy.umls_linking import UmlsEntityLinker

app = Flask(__name__)

# Load scispaCy model and UMLS linker ONCE on startup
nlp = spacy.load("en_core_sci_sm")
linker = UmlsEntityLinker()
nlp.add_pipe(linker)

def extract_umls_entities(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        for umls_ent in ent._.umls_ents:
            entities.append({
                "text": ent.text,
                "concept_id": umls_ent[0],
                "score": umls_ent[1]
            })
    return entities

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    input_text = ''
    if request.method == 'POST':
        input_text = request.form.get('text', '')
        results = extract_umls_entities(input_text)
    return render_template('index.html', input_text=input_text, results=results, mode='Dynamic')

if __name__ == '__main__':
    app.run(debug=True)
