import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

def generate_wordcloud(frequencies, output_path='static/charts/wordcloud.png'):
    plt.clf()

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis',
        contour_color='black',
        contour_width=1,
        prefer_horizontal=1.0,
        max_words=100,
        min_font_size=10
    ).generate_from_frequencies(frequencies)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches='tight', dpi=150)
    plt.close()

def get_top_frequencies(entity_list, top_n=30):
    from collections import Counter
    counter = Counter(entity_list)
    return dict(counter.most_common(top_n))
