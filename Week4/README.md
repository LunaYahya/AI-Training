# WEEK 4 EVALUATION, TUNING & PIPELINES
## Learning Objectives
- Understand the importance of train, validation, and test sets and how to use them correctly.
- Use cross-validation to get better estimates for the performance of your models.
- Identify whether your model suffers from underfitting or overfitting via the bias-variance tradeoff.
- Construct useful features and perform hyperparameter tuning on your models with the help of GridSearchCV.
- Construct pipelines for your models using Scikit-learn to avoid any data leakage.
## Key Topics
- Training/validation/test splits and avoiding leakage from the test set.
- k-fold and stratified cross-validation.
- Bias, variance, underfitting, and overfitting.
- Regularization techniques such as Ridge and Lasso.
- Feature engineering and transformations.
- Hyperparameters vs. model parameters.
- GridSearchCV and RandomizedSearchCV.
- Machine learning pipelines using Pipeline and ColumnTransformer.
- Optimizing full machine learning workflows.
- Comparing baseline and optimized model performance.
- Developing production-ready and reproducible machine learning workflows.
## Dataset Used
The (student_performance_dataset.csv) dataset has been used for the entire week four exercise in the process of model validation, feature engineering, and hyperparameter tuning. Some new features like [Study_Attendance_Index], [Past_Score_Study_Ratio], and [study_level] have been created out of the existing variables. The dataset was utilized in building an entire machine learning pipeline using preprocessing, feature engineering, and random forest classification techniques.
## Tools Used
- Scikit-learn (train_test_split, cross_val_score, StratifiedKFold, Ridge, Lasso, DecisionTree, GridSearchCV, RandomizedSearchCV, Pipeline, ColumnTransformer)
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git & GitHub
## Learning Outcomes
At the end of the week, I was able to learn the significance of splitting the dataset into training, validation, and test sets, as well as the role of cross-validation in obtaining a more accurate assessment of the model performance. I was able to detect overfitting and underfitting through bias-variance trade-off and use regularization for controlling the complexity of the model. I also learned about the proper way of designing features and tuning parameters using GridSearchCV. Lastly, I was able to create a full-fledged Scikit-learn pipeline including ColumnTransformer.
