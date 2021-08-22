from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import nltk
nltk.download("stopwords")
import pymorphy2
from collections import Counter
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
import re

morph = pymorphy2.MorphAnalyzer()
stop_words = stopwords.words("russian")

def to_ascii(s):
    try:
        s = s.replace("'", '').replace("-", '').replace("|", '')
        return s.decode('utf-8').encode("ascii", errors="ignore").decode()
    except:
        return ''

def is_asciiword(s):
    ascii_word = to_ascii(s)
    return len(ascii_word) > 2

def normal_rus(w):
    res = morph.parse(w)
    for r in res:
        if 'NOUN' in r.tag:
            return r.normal_form
    return None

def normal_eng(s):
    for sym in ("'s", '{', '}', "'", '"', '}', ';', '.', ',', '[', ']', '(', ')', '-', '/', '\\'):
        s = s.replace(sym, ' ')
    return s.lower().strip()

def get_word_cloud(txt):
  c_dict = Counter()
  for w in txt.split():
    if is_asciiword(w):
      # English word or digit
      n = normal_eng(w)
      c_dict[n] += 1
    else:
      # Russian word
      n = normal_rus(w)
      if n is not None and n not in stop_words:
        c_dict[n] += 1

  common = c_dict.most_common(100)
  wc = WordCloud(width=2600, height=2200, background_color="white", relative_scaling=1.0,
               collocations=False, min_font_size=10).generate_from_frequencies(dict(common))
  plt.axis("off")
  plt.figure(figsize=(9, 9))
  plt.imshow(wc, interpolation="bilinear")
  plt.xticks([])
  plt.yticks([])
  plt.tight_layout()
  file_name = 'words.png' 
  plt.savefig(file_name)