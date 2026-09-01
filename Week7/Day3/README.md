# Day 3 — RNNs & LSTMs for Sequential Data


## Learning Objectives


* Understand why sequential data requires order-aware architectures.
* Explain how Recurrent Neural Networks (RNNs) process sequential data using hidden states.
* Understand the vanishing-gradient problem in plain RNNs.
* Explain how LSTMs use gated memory to learn long-term dependencies.
* Understand the role of GRUs as a simpler gated recurrent architecture.
* Build and train an LSTM for ECG heartbeat classification.
* Compare a plain RNN with a tuned LSTM.
* Evaluate recurrent models using appropriate classification metrics.

## Key Topics


* Sequential Data
* Recurrent Neural Networks (RNNs)
* Hidden State and Memory
* Vanishing Gradient Problem
* Long Short-Term Memory (LSTM)
* Forget, Input, and Output Gates
* Gated Recurrent Units (GRUs)
* ECG Time-Series Classification
* Class Imbalance
* Classification Metrics
* Confusion Matrix
* Model Tuning
* Plain RNN vs LSTM

## Hands-On Lab (Tasks)

- Step 1: Build and train an LSTM on a sequential dataset (e.g. text sentiment or a time series) and record its
metric.
- Step 2: Compare the LSTM against a plain RNN or a non-sequential baseline and note the difference.
- Step 3: Explain, in Markdown, why order-awareness helped on this data.
- Step 4: Open a pull request with the current project notebook for the mid-sprint Mentor Code & Notebook
Review and address the feedback.

## Tools Used

* TensorFlow
* Keras
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* KaggleHub
* Google Colab
* Git / GitHub

## Learning Outcomes


At the end of the day, I was able to understand how RNNs process sequential data using hidden states, explain the limitations of plain RNNs and the vanishing-gradient problem, and understand how LSTMs use gated memory to preserve important information over time. I also built and trained LSTM and Plain RNN models for ECG heartbeat classification, applied model tuning and class weighting, evaluated the models using multiple classification metrics, and compared their performance.

The Tuned LSTM achieved **92.29% test accuracy** and **92.57% weighted F1-score**, outperforming the Plain RNN baseline with **82.78% test accuracy** and **75.12% weighted F1-score**.
