import os
import spacy
from collections import Counter

static_path = os.path.join("data", "umls_extracted_terms.txt")
with open(static_path, "r", encoding="utf-8") as f:
    STATIC_KEYWORDS = set(line.strip().lower() for line in f if line.strip())

def extract_static_entities(text):
    text_lower = text.lower()
    found = [kw for kw in STATIC_KEYWORDS if kw in text_lower]
    return list(set(found)), Counter(found)

def extract_dynamic_entities(text):
    try:
        import scispacy
        import en_core_sci_sm
        from scispacy.linking import EntityLinker
    except ImportError:
        return ["scispaCy or UMLS linker not available."], {}

    nlp = en_core_sci_sm.load()
    if "scispacy_linker" not in nlp.pipe_names:
        linker = EntityLinker(resolve_abbreviations=True, name="umls")
        nlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": True, "linker_name": "umls"})

    doc = nlp(text)
    entities = [ent.text.lower() for ent in doc.ents]
    return list(set(entities)), Counter(entities)

