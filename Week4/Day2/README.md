# Day 2 — Cross-Validation
## Learning Objectives
- Describe how k-fold cross-validation yields an accurate performance estimate.
- Perform cross-validation by utilizing cross_val_score and explain the mean and standard deviation.
- Describe the importance of stratified k-fold in classification.
## Key Topics
- Why is cross-validation superior to a one-off validation?
- How k-fold cross-validation works through rotating validation set.
- How to get a single score for each fold using cross_val_score.
- Interpretation of the mean and standard deviation of cross-validation scores.
- What is stratified k-fold and how does it work?
- Why is stratification essential in case of classification?
## Dataset Used
In order to learn how to assess the performance of models through cross-validation, a Week 3 classification data set was used (student_performance_dataset.csv). The data set was split into features (X) and target (y), and a Week 3 classification model was assessed with 5-fold cross-validation. Stratified k-fold cross-validation was also performed to maintain the proportion of classes in the folds.
## Hands-On Lab (Tasks)
- Step 1: Take a Week 3 model and evaluate it with 5-fold cross-validation using cross_val_score.
- Step 2: Report the mean and standard deviation of the scores across folds.
- Step 3: Compare the cross-validated estimate to the single-split score from Day 1 and explain any
difference.
- Step 4: For a classification task, confirm stratified folds are used and explain why that matters here.
## Tools Used
- Scikit-learn (cross_val_score, StratifiedKFold)
- Pandas
- Jupyter Notebook
## Learning Outcomes
By the end of the day, I was able to appreciate how cross-validation may be used to get a more reliable measure of the performance of a model compared to validation using one split. This is done by rotating the validation fold and training the model using the rest of the folds. In addition to this, I also learned how to perform cross-validation using cross_val_score function and understand the results in terms of mean and standard deviation of scores.
