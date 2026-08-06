# Day 5 — Supervised-Learning Mini-Project
## Learning Objectives
Build a fully  supervised learning pipeline starting with Exploratory Data Analysis (EDA) all the way to the modeling phase. Understand how to do basic pre-processing techniques such as encoding and scaling without leaking data into the future. Choose an appropriate machine learning model and evaluation technique for the task at hand, and finally compare your chosen model to a baseline model.
## Key Topics
- Complete Pipeline for Supervised Learning: EDA → preprocessing → train/test split → modeling → evaluation.
- Simple Preprocessing Steps: Dealing with missing data, one-hot encoding, and scaling features.
- Preventing Data Leakage: Applying the preprocessing operations only to the training set.
- Selection of Model and Metric: Deciding on the correct model and evaluation metric for the problem.
- Baseline: Checking how well the chosen model performs compared to a very simple baseline.
- Documentation: Documenting the entire process in a Jupyter Notebook.
## Dataset Used
A provided dataset was used to build an end-to-end supervised-learning mini-project(heart-Disease-Prediction.csv). The dataset was first explored using EDA to understand its structure, distributions, relationships, and potential data quality problems. After that, the data was divided into features (X) and target (y), followed by a train/test split to ensure that the models were evaluated on unseen data.
## Hands-On Lab (Tasks)
- Step 1: Choose a provided dataset and determine whether the task is regression or classification.
- Step 2: Perform brief EDA, then preprocess: handle missing values, encode categoricals, and scale features
(fit on train only).
- Step 3: Train at least two appropriate models and evaluate them with a suitable metric against a baseline.
- Step 4: Select the better model, justify the choice, and document the full pipeline in a narrated notebook.
- Step 5: Commit the finished mini-project notebook to GitHub with a clear commit message
## Tools Used
- Scikit-learn
- Pandas
- Matplotlib
-  Seaborn
- Jupyter Notebook
- Git & GitHub
## Learning Outcomes
Lastly, I understood how to construct a complete supervised learning pipeline starting from data exploration up until the point of evaluating the model. I understood how to conduct necessary preprocessing, including dealing with missing values, encoding categorical features, and scaling numeric features without data leakage, which means that preprocessing should be done only on the training data. Furthermore, I learned how to decide on which models to use and which evaluation metrics to use depending on the nature of the problem. Lastly, I understood how to compare different models against the baseline model, find out which is the best performing model, justify my decision, and document everything in a Jupyter Notebook.
