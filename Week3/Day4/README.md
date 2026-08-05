# Day 4 — Trees, Forests, SVMs & k-NN
## Learning Objectives
Develop decision trees and random forests, along with interpreting them, especially their features' importance.
Discover how support vector machines (SVMs) and k-nearest neighbors (k-NN) classifiers work to classify data.
Evaluate several classification models using the same data and evaluation metric.
## Key Topics
Decision Trees: rule-based models, interpretability, and overfitting.
Random Forests: ensemble learning and feature importances.
Support Vector Machines (SVM): decision boundaries and margins.
k-Nearest Neighbors (k-NN): classification based on nearby data points.
Comparing different classification models fairly.
## Dataset Used
The classification dataset used on Day 3 (healthcare-dataset-stroke-data.csv) was the same dataset used in this experiment. The dataset was partitioned into features (X) and target (y). It was further partitioned into training and testing datasets to make sure that all the classification models are evaluated using the same data.
## Hands-On Lab (Tasks)
- Step 1: Train a decision tree, random forest, SVM, and k-NN on the same train/test split from Day 3.
- Step 2: Evaluate all four with the same metric (e.g. F1-score) and assemble the results into one comparison
table.
- Step 3: Report the random forest's top feature importances and interpret them.
- Step 4: Identify the best-performing model for this dataset and explain, in Markdown, why it likely won.
## Tools Used
- Scikit-learn (DecisionTreeClassifier, RandomForestClassifier, SVC, KNeighborsClassifier)
- Pandas
- Jupyter Notebook
## Learning Outcomes
Finally, I learned about various classification models such as Decision Trees, Random Forest, Support Vector Machine (SVM), and k-Nearest Neighbor (k-NN). I learned about how the Decision Tree model uses a series of rules to make a prediction, and how the Random Forest improves accuracy by combining multiple decision tree models. In addition, I learned how the Support Vector Machine constructs the decision boundary through maximizing the margins between classes and how the k-Nearest Neighbor model classifies new data based on the closest training set. Finally, I learned how to perform a fair comparison among the models by training them using the same data with the same train/test split and same metrics.
