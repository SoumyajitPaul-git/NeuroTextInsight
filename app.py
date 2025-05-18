from flask import Flask, render_template, request
from utils.extract_entities import extract_static_entities, extract_dynamic_entities
from utils.generate_visuals import generate_wordcloud
import os
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    frequencies = {}
    chart_url = ""
    mode = "static"
    input_text = ""

    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        mode = request.form.get('mode', 'static')

        if input_text.strip():
            if mode == 'dynamic':
                results, frequencies = extract_dynamic_entities(input_text)
            else:
                results, frequencies = extract_static_entities(input_text)

            if results:
                unique_id = str(uuid.uuid4())
                chart_path = os.path.join('static', 'charts', f'wordcloud_{unique_id}.png')
                generate_wordcloud(frequencies, chart_path)
                chart_url = f'charts/wordcloud_{unique_id}.png'  # relative to static folder

    return render_template(
        "index.html",
        entities=results,
        frequencies=frequencies,
        chart=chart_url,
        mode=mode,
        input_text=input_text
    )

if __name__ == '__main__':
    os.makedirs("static/charts", exist_ok=True)
    app.run(debug=True)
