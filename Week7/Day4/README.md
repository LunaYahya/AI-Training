# Day 4 — Transformers & NLP

## Learning Objectives
* Understand the Transformer architecture and the role of self-attention.
* Load and use a pre-trained Transformer model for text classification.
* Apply a pre-trained DistilBERT model to the project data.
* Compare Transformer performance with an LSTM-based approach.
* Understand how attention differs from RNN step-by-step memory.
* Select the most suitable architecture for the project based on experimental results.

## Key Topics

* Transformers
* Self-Attention
* Attention Mechanism
* Natural Language Processing (NLP)
* Pre-trained Models
* DistilBERT
* Hugging Face Transformers
* Text Classification
* Fine-Tuning
* LSTM vs. Transformer
* Model Evaluation

## Hands-On Lab (Tasks)

- Step 1: Load a pre-trained transformer with the Hugging Face pipeline and run it on sample text.
- Step 2: If the project is text-based, apply the transformer to the project data and compare its metric to the Day 3 LSTM.
- Step 3: Explain, in Markdown, in one paragraph, how attention differs from an RNN's step-by-step memory.
- Step 4: Record which architecture (LSTM vs. transformer) will serve as the project's core model and why.


## Tools Used

* TensorFlow
* Keras
* Hugging Face Transformers
* DistilBERT
* NumPy
* Pandas
* Scikit-learn
* Google Colab
* Git / GitHub

## Results

### DistilBERT

* Accuracy: **89.60%**
* Weighted Precision: **89.53%**
* Weighted Recall: **89.60%**
* Weighted F1-score: **89.40%**

### Text LSTM

* Accuracy: **13.40%**
* Weighted Precision: **1.80%**
* Weighted Recall: **13.40%**
* Weighted F1-score: **3.17%**

DistilBERT achieved substantially better performance than the Text LSTM on the Day 4 sentiment classification task. The LSTM showed a strong bias toward a single class, while DistilBERT achieved strong performance across all three sentiment classes.

## Learning Outcomes

At the end of the day, I was able to understand the Transformer architecture and self-attention mechanism, load and fine-tune a pre-trained DistilBERT model for text classification, evaluate its performance using classification metrics, compare the Transformer with an LSTM approach, and select DistilBERT as the core architecture for the sentiment classification task based on the experimental results.
