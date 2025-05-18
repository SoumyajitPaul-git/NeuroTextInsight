
# 🧠 NeuroText Insight

**NeuroText Insight** is a web-based biomedical NLP tool that intelligently extracts neurodegeneration-related entities from research text using both static keyword matching and dynamic deep-learning-based techniques (via **scispaCy**). It provides visual insights into term frequency and generates word clouds to assist neuroscience and biomedical researchers.

![NeuroText Insight Screenshot](static/demo_screenshot.png)

---

## 🚀 Features

- 📝 **Text Input**: Paste any biomedical or neuroscience-related text
- 🔍 **Entity Extraction**:
  - **Static Mode**: Matches text against a curated set of UMLS-based keywords
  - **Dynamic Mode**: Uses `scispaCy` + `UMLS linker` for advanced biomedical NER
- 📊 **Frequency Analysis**: Displays term frequencies in the submitted text
- ☁️ **Word Cloud Visualization**: Generates a word cloud for visual exploration of terms
- 🔄 **Toggle Mode**: Switch between static and dynamic modes based on context
- 🖼️ **Interactive UI**: Beautifully styled HTML UI with modern look and feel
- 📁 **Offline Support**: Works without internet (static mode only)

---

## 📂 Project Structure

```
neurotext-insight/
│
├── app.py                         # Flask application
├── templates/
│   └── index.html                 # Main UI template
├── utils/
│   ├── extract_entities.py       # Static & dynamic entity extractors
│   └── generate_visuals.py       # Frequency chart & word cloud generator
│
├── data/
│   └── umls_extracted_terms.txt  # Keyword list for static mode
│
├── static/
│   └── charts/                   # Word clouds are saved here
│
└── README.md                     # This file
```

---

## 📦 Requirements

- Python 3.8+
- Flask
- matplotlib
- wordcloud
- scispaCy *(for dynamic mode)*
- en_core_sci_sm
- scispacy-linker

---

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/neurotext-insight.git
cd neurotext-insight
```

2. **Set up a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. *(Optional)* For **dynamic mode**, install scispaCy models:
```bash
pip install scispacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz
pip install scispacy[linking]
```

---

## ▶️ Running the App

```bash
python app.py
```

- Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Paste your biomedical text and click **"Analyze"**

---

## 🧪 Example Text (Try this!)

Copy-paste this into the text area:

> Alzheimer’s disease is marked by amyloid-beta plaques and tau neurofibrillary tangles in regions such as the hippocampus and cerebral cortex. Recent therapies including aducanumab and lecanemab target Aβ clearance, while new genetic approaches like CRISPR-Cas9 aim at editing APOE4 risk variants.

---

## 📊 Output

- **Entities List**: Extracted biomedical terms
- **Frequencies**: Word counts for key terms
- **Word Cloud**: Visual summary of important entities

---

## ⚙️ Modes Explained

| Mode     | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| Static   | Fast & offline. Matches known terms from `umls_extracted_terms.txt`        |
| Dynamic  | Uses `scispaCy + UMLS linker` for real-time NER, requires internet & model |

---

## 📌 Notes

- Dynamic mode may take longer to load due to model initialization
- If you want to skip installing the large `UMLS` model, use **Static Mode** only
- Word cloud image is auto-saved to `static/charts/`

---

## 💡 Future Improvements

- Highlighting entities inside the original text
- Support for multi-language biomedical content
- Export results as PDF or CSV
- Enhanced charts and graphs with interactivity

---

## 🧑‍💻 Author

**Your Name**  
*Biomedical NLP & AI Research Enthusiast*  
GitHub: [@yourusername](https://github.com/yourusername)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Show your support

If you found this helpful, give the repo a ⭐ and share it with your peers!
