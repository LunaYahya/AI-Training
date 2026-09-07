# Day 2 — Text Representation: TF-IDF & Embeddings

## Learning Objectives

- Understand how cleaned text is converted into numerical representations.
- Apply Bag-of-Words and TF-IDF to the project data.
- Train a Logistic Regression classifier using TF-IDF features.
- Understand word embeddings and how they represent semantic relationships.
- Use pre-trained GloVe embeddings to explore semantic geometry.
- Understand contextual embeddings and their connection to DistilBERT.
- Compare TF-IDF with the previous LSTM and DistilBERT models.
- Select the most suitable text representation for the sentiment classification project.

## Key Topics

- TF-IDF
- Bag-of-Words
- Sparse and Dense Representations
- Word Embeddings
- Word2Vec and GloVe
- Semantic Geometry
- Nearest Neighbors
- Contextual Embeddings
- DistilBERT
- Text Classification
- Model Evaluation
- TF-IDF vs. Embeddings

## Hands-On Lab (Tasks)

- Step 1: Apply TF-IDF to the cleaned text from Day 1 and train a simple classifier as a text baseline.
- Step 2: Load pre-trained word embeddings and find the nearest neighbors of a few words to see the semantic geometry.
- Step 3: If the project is text-based, compare a TF-IDF model against the Week 7 LSTM/transformer on the same metric.
- Step 4: Document which representation fits the project and why, in Markdown.

## Tools Used

- Scikit-learn
- Gensim
-GloVe Pre-trained Embeddings
- Hugging Face Transformers
- DistilBERT Tokenizer
- NLTK
- NumPy
- Pandas
- Google Colab
- Git / GitHub

## Results

### TF-IDF + Logistic Regression

| Metric | Result |
|---|---:|
| Accuracy | 89.80% |
| Weighted Precision | 89.69% |
| Weighted Recall | 89.80% |
| Weighted F1-score | 89.68% |

### Previous Model Results

| Model | Accuracy | Weighted Precision | Weighted Recall | Weighted F1-score |
|---|---:|---:|---:|---:|
| Text LSTM | 63.40% | 40.20% | 63.40% | 49.20% |
| DistilBERT | 89.60% | 89.53% | 89.60% | 89.40% |

TF-IDF achieved strong results as a traditional baseline and performed competitively with DistilBERT on this dataset. However, TF-IDF does not understand semantic meaning or context. DistilBERT remains the preferred core representation because it captures contextual relationships between words.

## Learning Outcomes

At the end of the day, I was able to convert cleaned text into TF-IDF vectors, explain Bag-of-Words and word embeddings, load pre-trained GloVe embeddings, inspect semantic neighbors and word analogies, understand contextual Transformer embeddings, compare TF-IDF with LSTM and DistilBERT, and select DistilBERT as the core representation while keeping TF-IDF as a strong traditional baseline.


