# Day 4 — Feature Engineering & Hyperparameter Tuning 
## Learning Objectives
- Add new features and perform transformations accordingly.
- Differentiate between hyperparameters and learned parameters.
- Perform tuning of a machine learning model by employing GridSearchCV along with cross-validation.
- Know about the application of RandomizedSearchCV on large hyperparameters.
## Key Topics
- Feature engineering and the ways that improved features can help improve model results.
- Popular feature engineering methods include creating new features, binning, encoding, datetime extraction, and scaling.
- Hyperparameters and learned parameters.
- GridSearchCV and cross-validation.
- What is param_grid, best_params_, best_score_, and best_estimator_?
- RandomizedSearchCV for large hyperparameter spaces.
- Tuned models vs. baseline models.
## Dataset Used
The (student_performance_dataset.csv) dataset was used for feature engineering and hyperparameter optimization. New features such as [Study_Attendance_Index
] , [Past_Score_Study_Ratio],[study_level] were generated using the existing features to provide more information to the model. Using the dataset, a machine learning model was trained. The process of determining the best hyperparameters of the model was performed using GridSearchCV with five-fold cross-validation.
## Hands-On Lab (Tasks)
- Step 1: Create at least two new engineered features for a provided dataset and justify each in Markdown.
- Step 2: Define a hyperparameter grid for a model from Week 3 (e.g. random forest).
- Step 3: Run GridSearchCV with 5-fold cross-validation and report the best parameters and score.
- Step 4: Compare the tuned model's cross-validated score against the untuned baseline from Week 3.
- Step 5: Document which engineered feature and which hyperparameter mattered most.
## Tools Used
- Scikit-learn (GridSearchCV, RandomizedSearchCV, RandomForestClassifier)
- Pandas
- Jupyter Notebook
- Numpy
- Math
- Matplotlib
## Learning Outcomes
In the end of the day, I was able to generate useful features using existing data and comprehend the role that feature engineering plays in enhancing the effectiveness of the model. I was able to distinguish between model parameters and hyperparameters and comprehend the importance of choosing hyperparameters before fitting the model because I was aware of the fact that hyperparameters have to be chosen before fitting the model. I learned about the process of using GridSearchCV along with cross validation for the selection of best hyperparameters rather than manually selecting hyperparameters. Moreover, I learned about the role of RandomizedSearchCV when there are numerous possibilities of hyperparameters.
