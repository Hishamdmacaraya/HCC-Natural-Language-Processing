# Importing necessary libraries
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Sample corpus
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
]

# ---- Bag of Words (BoW) ----
# Using CountVectorizer to convert text to BoW representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print("Bag of Words (BoW) Representation:\n", X.toarray())

# ---- TF-IDF ----
# Using TfidfVectorizer to convert text to TF-IDF representation
tfidfvectorizer = TfidfVectorizer()
X_tfidf = tfidfvectorizer.fit_transform(corpus)
print("\nTF-IDF Representation:\n", X_tfidf.toarray())

# ---- Feature Engineering ----
# 1. Text Length
text_length = [len(doc) for doc in corpus]
print("\nText Length Feature:", text_length)

# 2. Number of Unique Words
num_unique_words = [len(set(doc.split())) for doc in corpus]
print("\nNumber of Unique Words Feature:", num_unique_words)
