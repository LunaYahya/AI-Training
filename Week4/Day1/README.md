# Day 1 — Train / Validation / Test Splits
## Learning Objectives
- Explain the need for having a validation set in addition to the test set.
- Perform the appropriate three-way split using Scikit-learn.
- Explain why tuning the model with the help of the test set might be misleading.
- Learn about the significance of keeping the test set untouched until the end.
## Key Topics
- The drawbacks of having only one test set to perform the tuning.
- Three-way splitting of data into training, validation, and test sets.
- Making the train, validation, and test sets using train_test_split.
- Knowing about data leakage and why the test set shouldn't be used in the process of building the model.
- Shortcomings of using one validation set and the reason behind cross-validation.
## Dataset Used
For the purpose of learning how to divide a dataset into training, validation, and test sets, a Week 3 dataset was utilized(student_preformance_dataset.csv)
First of all, the dataset was divided into X (feature set) and y (target set). Further, it was divided into three distinct sets for proper tuning of the model and its evaluation.
## Hands-On Lab(Tasks)
- Step 1: Take a Week 3 dataset and create a 60/20/20 train/validation/test split with a fixed random_state.
- Step 2: Train a model on the training set and tune one setting by checking the validation set only.
- Step 3: Evaluate the final model on the test set exactly once and report the score.
- Step 4: In Markdown, explain what would go wrong if you had tuned against the test set instead.
## Tools Used
- Scikit-learn (train_test_split)
- Pandas
- Jupyter Notebook
## Learning Outcomes
By the time the day ended, I got to know the significance of separating data into three parts, i.e., training set, validation set, and test set. I was also made aware that the training set will help in training the model while the validation set helps in tuning the model and making developmental decisions. In addition, I came to learn that using the test set again and again during the process of tuning of the model leads to information leakage and gives an optimistic performance evaluation of the model.
