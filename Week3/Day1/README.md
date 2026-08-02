### Day 1 – Introduction to Supervised Learning Concepts and the Scikit-learn API

On Day 1, we have learned the basic principles of supervised machine learning and the basic steps followed when training and testing machine learning algorithms. This includes understanding the workings of supervised learning on labelled datasets, and differentiating between regression and classification problems. In addition, we have learned how to split a dataset into the features and targets (X and y), split into train and test sets, and work with the uniform Scikit-learn API to implement machine learning algorithms.
## Learning Objectives
In today’s session, we have learnt how to describe supervised learning and how to differentiate regression from classification problems. We have also learned how to divide the data into features (X) and targets (y) and conduct an 80/20 train-test split. In addition to that, we have learned the importance of validating a model using test data, which it hasn’t seen before.
## Key Concepts
- Supervised Learning: Machine learning technique where the model learns from the labeled dataset, which means that the output or target is known beforehand. The model learns the mapping between the input feature and the output/target in order to predict the output for new observations.
- Regression Vs. Classification: Regression is applied when the target or output is numeric, such as housing price, temperature, etc. The Classification model is applied when the output or target denotes a certain class or category, such as spam or non-spam, etc.
- Features Vs. Target: Features (X) are the inputs or columns used by the model for learning whereas the Target (y) is the output or the column predicted by the model.
- API for Scikit-Learn: The Scikit-Learn library offers a uniform application programming interface for machine learning models. The API consists of four major steps: instantiate, fit, predict and score. A consistent API makes it much easier to implement any machine learning algorithm.
- Train/ Test Split: Splitting the dataset into two parts makes it possible to train the model on one dataset while evaluating it on another. That way, the results will be closer to reality since the model is evaluated on unseen data.
- Model Evaluation: Any machine learning model must be evaluated on unseen test data. Evaluating the performance of a model on training data is not an appropriate approach since it can lead to misleading results when the model just memorizes training examples.
## Tools Used
- Python
- Scikit-learn
- Pandas
- Jupyter Notebook
## Dateset Used 
 A given dataset was applied for performing the Tasks(student_performace_dataset.csv) to gain knowledge about the process of supervised learning. The dataset was divided into features (X) and target (y), and then split into training and testing datasets to get ready for the machine learning process.
## Hands-On Lab (Tasks)
- Step 1: Load a provided dataset and separate it into features X and target y.-
- Step 2: Perform an 80/20 train/test split with a fixed random_state.
- Step 3: Confirm the shapes of X_train, X_test, y_train, y_test are consistent and print them.
- Step 4: In a Markdown cell, explain in your own words why the model must never see the test set during training.
## Learning Outcomes
One of the learning outcomes for the day was gaining an understanding of the basics of supervised learning and the two most common types of algorithms – regression and classification. I have had hands-on experience on how to distinguish features from the target and splitting of data into train and test sets. Moreover, I learned how important it is to test the model on the unseen data. The Scikit-learn API and general machine learning pipeline (instantiate, fit, predict, and score) were introduced for future use.
