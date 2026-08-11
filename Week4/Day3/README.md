# Day 3 — Bias-Variance & Diagnosing Model Fit
## Learning Objectives
- Describe the symptoms of underfitting and overfitting.
- Describe the bias-variance trade-off and explain its importance in tuning models.
- Determine model fit through the train/validation score difference.
- Perform regularization by using Ridge (L2) and Lasso (L1) methods to reduce overfitting.
## Key Topics
- Underfitting (high bias) vs overfitting (high variance).
- The Bias-Variance Trade-off.
- Determining model fitting through training and validation accuracy.
- Interpreting the difference between training and validation accuracy.
- Regularization and its significance in mitigating overfitting.
- Ridge regression (L2) and Lasso regression (L1).
- The influence of the alpha value in regularization.
- Decreasing model complexity for better generalization.
## Dataset Used
A dataset for classification was chosen to practice determining the fitting of the model and the performance of the model. X and y variables were separated from the dataset and split into the training and validation datasets.
The Decision Tree was chosen as a model to show both underfitting and overfitting through changing the complexity of the model. Ridge and Lasso regressions were also used.
## Hands-On Lab (Tasks)
- Step 1: Deliberately overfit a model (e.g. a very deep decision tree) and confirm the large train-vsvalidation gap.
- Step 2: Deliberately underfit a model (e.g. an overly simple one) and confirm both scores are low.
- Step 3: Apply regularization (or reduce complexity) to the overfit model and show the gap shrink.
- Step 4: Document each diagnosis and fix with the score evidence in Markdown.
## Tools Used
- Scikit-learn (DecisionTreeRegressor, Ridge, Lasso, StandardScaler, R²)
- Pandas
- Matplotlib
- Jupyter Notebook
## Learning Outcomes
At the end of the day, I was able to tell the difference between underfitting and overfitting based on training and validation scores. I got to know about the influence of bias-variance trade-off on model complexity and how the train-validation gap is used to identify problems with model fitting.
Apart from that, I learned how simplifying the model prevents overfitting and how regularization, namely Ridge (L2) and Lasso (L1), controls model complexity. Moreover, I understood how the alpha value influences regularization and how models are compared according to their training and validation scores.
