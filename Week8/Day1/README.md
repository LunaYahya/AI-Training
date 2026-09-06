# Day 1 — Sprint 3 Planning & NLP Preprocessing

## Learning Objectives

* Define the Sprint 3 goal and integration and evaluation backlog.
* Explain why raw text requires preprocessing before numerical representation.
* Apply word-level and sub-word tokenization.
* Apply lowercasing, punctuation handling, stop-word handling, and lemmatization.
* Preserve sentiment-critical negations such as `not`, `no`, and `never`.
* Document preprocessing decisions and their connection to the selected model architecture.

## Topics Covered

* Sprint 3 planning and backlog definition.
* Improvements carried forward from the Sprint 2 retrospective.
* Text preprocessing for sentiment classification.
* Word tokenization with NLTK.
* Sub-word tokenization with the DistilBERT tokenizer.
* Lowercasing and punctuation handling.
* Stop-word removal with protected negations.
* Lemmatization and comparison with stemming.
* Task-dependent preprocessing for Transformer models.
* Before-and-after text comparison and vocabulary analysis.

## Hands-On Lab

- Step 1: Complete Sprint 3 planning and select the backlog tasks for integration and evaluation.
- Step 2: Take a raw text sample (or the project's text data) and tokenize it.
- Step 3: Apply a full cleaning pipeline: lowercase, remove punctuation, remove stop words, lemmatize.
- Step 4: Verify the cleaning preserves task-critical words (e.g. negations for sentiment) and document the choices in Markdown.

## Tools Used

* Python
* NLTK
* Pandas
* Scikit-learn
* Hugging Face Transformers
* DistilBERT Tokenizer
* Google Colab
* KaggleHub

## Deliverables

* Sprint 3 goal and backlog.
* Word-tokenization demonstration.
* DistilBERT sub-word-tokenization demonstration.
* Reusable text-preprocessing function.
* Lemmatization and stemming comparison.
* Cleaned Google Play review dataset in the `clean_text` column.
* Before-and-after review comparison.
* Vocabulary-size comparison.
* Negation-preservation tests.
* Markdown documentation of preprocessing decisions.
* Final Day 1 summary.

## Summary
Day 1 focused on planning Sprint 3 and preparing the project review data for the next stages of the NLP pipeline.
The main outcome was a reusable preprocessing workflow that handles traditional text-cleaning tasks while protecting sentiment-critical negations. Word-level and sub-word tokenization were also compared, highlighting the difference between traditional NLP preprocessing and the requirements of Transformer-based models such as DistilBERT.
