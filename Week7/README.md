# Week 7 — Deep Learning: CNNs, RNNs, LSTMs & Transformers

## Overview

This week focused on advancing Deep Learning skills by applying different neural network architectures to image, sequential, and text data.

The week covered **CNNs, Data Augmentation, Transfer Learning, RNNs, LSTMs, GRUs, Transformers, and Hyperparameter Tuning**, with practical applications on image classification, ECG heartbeat classification, and sentiment analysis.

## Learning Objectives

* Build and evaluate CNN models for image classification.
* Apply data augmentation to improve model generalization.
* Use Transfer Learning with pre-trained models such as MobileNetV2.
* Understand how RNNs process sequential data.
* Build and tune LSTM models for time-series classification.
* Understand Transformers and the Self-Attention mechanism.
* Apply DistilBERT for text classification.
* Compare different Deep Learning architectures.
* Tune the core model and track experiments.
* Evaluate models using appropriate classification metrics.
* Complete Sprint 2 Review and Retrospective.

## Weekly Structure

| Day       | Topic                             | Main Focus                                                |
| --------- | --------------------------------- | --------------------------------------------------------- |
| **Day 1** | CNNs & Transfer Learning          | CNN from scratch, Data Augmentation, MobileNetV2          |
| **Day 2** | Building CNNs & Transfer Learning | CNN architecture, pooling, augmentation, model comparison |
| **Day 3** | RNNs & LSTMs                      | Sequential data, RNN, LSTM, GRU, ECG classification       |
| **Day 4** | Transformers & NLP                | Self-Attention, DistilBERT, Text Classification           |
| **Day 5** | Core Model & Sprint Review        | Model tuning, experiments, evaluation, Sprint Review      |

## Projects & Applications

###  Image Classification

Built CNN models for skin cancer image classification and explored:

* CNN from scratch
* Data Augmentation
* Transfer Learning
* MobileNetV2
* Training and validation curves
* Accuracy and training-time comparison

###  ECG Heartbeat Classification

Applied recurrent neural networks to sequential ECG data:

* Plain RNN
* LSTM
* GRU concepts
* Class weighting
* Model tuning
* Confusion Matrix
* Classification metrics

The tuned LSTM achieved **92.29% test accuracy** and **92.57% weighted F1-score**, outperforming the Plain RNN baseline.

### 💬 Sentiment Classification

Applied Transformer-based NLP models to text classification:

* Transformer architecture
* Self-Attention
* DistilBERT
* Hugging Face Transformers
* LSTM vs Transformer comparison

DistilBERT achieved **89.60% accuracy**, substantially outperforming the Text LSTM on the sentiment classification task.

## Model Development & Evaluation

The final stage focused on improving the project's core model through:

* Hyperparameter tuning
* Experiment tracking
* Training and validation curves
* Confusion Matrix
* Classification metrics
* Model comparison
* Saving the best-performing model

## Tools & Technologies

* Python
* TensorFlow / Keras
* Scikit-learn
* Hugging Face Transformers
* DistilBERT
* NumPy
* Pandas
* Matplotlib
* imbalanced-learn (SMOTE)
* Google Colab
* Git & GitHub
* MLflow *(optional)*

## Key Outcomes

By the end of Week 7, I was able to:

* Build and train different Deep Learning architectures.
* Understand when to use CNNs, RNNs, LSTMs, and Transformers.
* Apply Transfer Learning using a pre-trained model.
* Work with image, sequential, and text data.
* Improve model performance through tuning.
* Compare models using multiple evaluation metrics.
* Track experiments and select the best-performing model.
* Complete the Sprint 2 Review and Retrospective.

## Deliverables

* CNN models and experiments
* Transfer Learning model
* RNN and LSTM experiments
* Transformer / DistilBERT model
* Experiment log
* Model comparison table
* Training and validation curves
* Confusion Matrix
* Evaluation metrics
* Saved best model
* Sprint 2 Review
* Sprint 2 Retrospective
