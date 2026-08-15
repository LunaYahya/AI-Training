 # Cardiac Patient Monitoring System - Student Individual Project
## Project Objective
- Create a machine learning classification workflow for health data related to heart disease.
- Perform data cleaning and exploration using Pandas, NumPy, Matplotlib, and Seaborn.
- Define a supervised learning problem for predicting `HeartDiseaseorAttack`.
- Train and compare classification models.
- Evaluate model performance using classification metrics and cross-validation.
- Engineer new features from existing ones.
- Develop Scikit-learn Pipelines to integrate feature engineering, preprocessing, and modeling into a reproducible workflow
## Dataset Use
The **Heart Disease Health Indicators Dataset** was used in this project. The dataset contains health, lifestyle, and demographic indicators related to heart disease.
**Target variable:** HeartDiseaseorAttack represents whether an observation belongs to the reported heart disease or heart attack class.
## Data Preparation & EDA
- Cleaned the dataset by removing duplicate observations.
- Checked missing values, descriptive statistics, class balance, and correlations.
- Conducted exploratory data analysis using visualizations with Matplotlib and Seaborn.
## Supervised Learning
A binary classification task was defined using HeartDiseaseorAttack as the target variable
Two models were trained and compared:
- Logistic Regression
- Random Forest
## Model Evaluation
Models were compared using accuracy, precision, recall, F1-score, confusion matrix, and 5-fold stratified cross-validation.
Logistic Regression achieved the best original F1-score (**0.2014**) compared with Random Forest (**0.1768**).
## Feature Engineering & Pipelines
Three new features were engineered:
- BMI_Category
- Age_Group
- Health_Burden
Scikit-learn Pipelines were used to create a reproducible workflow combining feature engineering, preprocessing, and model training.
The Logistic Regression Pipeline achieved the best pipeline F1-score (**0.1952**) compared with the Random Forest Pipeline (**0.1706**).
## Tools Used
- Python
- Scikit-learn (train_test_split, StratifiedKFold, cross_val_score, LogisticRegression,RandomForestClassifier, StandardScaler,Pipeline,classification metrics)
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git & GitHub
## Learning Outcomes
As a result of this project, I was able to clean and analyze a health-related real-world dataset using Pandas and NumPy, conduct descriptive statistics and exploratory data analysis, and identify data quality issues such as duplicates and class imbalance.
I was also able to define a supervised classification problem, develop a baseline Logistic Regression model, compare it with a Random Forest classifier, and evaluate both models using accuracy, precision, recall, F1-score, confusion matrices, and cross-validation.
Additionally, I gained experience in creating useful features from existing health indicators and constructing Scikit-learn Pipelines that combine feature engineering, preprocessing, and model training.
Logistic Regression outperformed Random Forest based on F1-score, while class imbalance remained a significant challenge.
## Limitations
- The target variable is highly imbalanced.
- Although the models achieved high overall accuracy, recall and F1-score for the positive class were relatively low.
- Feature engineering did not produce a significant improvement in test-set F1-score.
- The project is intended for educational machine learning purposes and is not a clinical diagnostic system.
