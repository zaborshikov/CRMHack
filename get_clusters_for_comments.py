from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

def get_clusters_for_comments(documents: list, n_clusters=40): 
  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(documents)

  true_k = n_clusters
  model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
  model.fit(X)

  order_centroids = model.cluster_centers_.argsort()[:, ::-1]
  terms = vectorizer.get_feature_names()
  return [[Y, model.predict(vectorizer.transform([Y]))[0]] for Y in documents]