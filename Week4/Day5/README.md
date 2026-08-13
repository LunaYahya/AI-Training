# Day 5 — Scikit-learn Pipelines & Tuned Mini-Project
## Learning Objectives
Learning Objectives
- create a Pipeline that integrates preprocessing and modeling without introducing data leakage.
- Apply ColumnTransformer for different preprocessing of numerical and categorical variables.
- Tune an entire machine learning Pipeline with GridSearchCV in 5-fold cross-validation.
- Test the final tuned Pipeline on the hold-out test set against the baseline model.
## Key Topics
- Why Pipelines help prevent data leakage.
- Building a Pipeline that combines feature engineering, preprocessing, and modeling.
- ColumnTransformer for handling mixed numerical and categorical data.
- Hyperparameter tuning of a complete Pipeline using GridSearchCV.
- Using F1-score for the Fail class when dealing with imbalanced data.
- Comparing cross-validation results with final test performance.
- Building a professional, reproducible, and leak-free machine learning workflow.
## Dataset Used
The (student_performance_dataset.csv) dataset was employed in the creation of an end-to-end machine learning pipeline. The features that had been engineered on Day 4, such as [Study_Attendance_Index], [Past_Score_Study_Ratio], and [study_level], were included in the Pipeline. Separate processes were used to preprocess the numerical and categorical features using the ColumnTransformer approach. The Random Forest classifier was used to make the predictions. The GridSearchCV technique with five-fold cross-validation was employed to fine-tune the entire Pipeline.
## Hands-On Lab (Tasks)
- Step 1: Build a Pipeline with a ColumnTransformer handling numeric (scaling) and categorical (encoding)
columns.
- Step 2: Add the engineered features from Day 4 into the workflow.
- Step 3: Tune the full pipeline with GridSearchCV and 5-fold cross-validation.
- Step 4: Evaluate the final tuned pipeline once on the held-out test set and report the metric against a
baseline.
- Step 5: Commit the finished pipeline notebook to GitHub with a clear commit message
## Tools Used
- Scikit-learn (Pipeline, ColumnTransformer, GridSearchCV, RandomForestClassifier)
- Pandas
- Jupyter Notebook
- Git & GitHub
## Learning Outcomes
In the end of the day,I have managed to construct an end-to-end Machine Learning pipeline which takes care of feature engineering and processing and building the model without any data leakage. I have learned to utilize ColumnTransformer for different treatment of numeric and categorical variables and to optimize the whole process using GridSearchCV with five folds validation. In addition to this, I have learned to evaluate the optimized model using test data and F1 score for Fail class.
