# Day 3 — Logistic Regression & Classification Metrics 
## Learning Objectives
- Fit a Logistic Regression model and make predictions of classes and probabilities.
- Learn about the limitation of using only accuracy to evaluate classifiers, particularly for imbalanced datasets.
- Analyze the confusion matrix by understanding TP, TN, FP, and FN.
- Assess classifiers by using precision, recall, F1-score, and AUC-ROC.
## Key Topics
- Logistic Regression: weight * sum + sigmoid = probability
- Classification versus regression
- Why accuracy can be a poor metric for imbalance
- The confusion matrix: TP, TN, FP, FN
- Precision, Recall, and F1-score
- The precision vs. recall trade-off
-  AUC-ROC and discrimination ability
## Dataset Used
A provided classification dataset (healthcare-dataset-stroke-data.csv)was used to perform the hands-on tasks and understand the process of building and evaluating a classification model. The dataset was divided into features (X) and target (y) and then split into training and testing datasets.
## Hands-On Lab (Tasks)
- Step 1: Train a LogisticRegression model on a provided classification dataset (e.g. churn).
- Step 2: Generate predictions and produce the confusion matrix.
- Step 3: Compute precision, recall, and F1 with classification_report, and interpret each.
- Step 4: Decide whether precision or recall matters more for this specific problem and justify it.
- Step 5: Compute the AUC-ROC and document what it says about the model.
## Tools Used
- Scikit-learn (LogisticRegression)
-   Pandas
-    Matplotlib
-  Jupyter Notebook
## Learning Outcomes
At the end of the day, I learned about the concepts of logistic regression and how it could be applied for solving classification problems. This included training a classification model, making predictions and class probabilities and interpreting the confusion matrix. Furthermore, I have learned about evaluation of the classification performance using metrics such as precision, recall, f1-score, and AUC-ROC. I have learned why accuracy is not always enough for evaluating a model's performance, especially in cases where the data is imbalanced.
