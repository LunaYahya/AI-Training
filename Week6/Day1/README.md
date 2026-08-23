Day 1 — Sprint 1 Planning & Neural Network Architecture
Learning Objectives
Plan Sprint 1 and create a baseline model for the project.
Learn about the significance of creating a baseline before moving to other models.
Learn about how a single neuron consists of weighted sum, bias, and activation function.
Learn about how input layer, hidden layer, and output layer work in Neural Networks.
Learn about “deep” in Deep Learning.
Learn about weights and biases in Neural Network.
Create an initial Neural Network architecture for the project.
Key Topics
Sprint 1 Planning
Sprint Goal & Backlog
Baseline First Approach
Dataset Completion
Exploratory Data Analysis (EDA)
Class Imbalance Problem
Training & Test Set Splitting
SMOTE
Logistic Regression Baseline
Baseline Metrics
Why Deep Learning?
The Neuron
Weighted Sum, Bias & Activation Function
Layers of a Neuron
Weights & Bias in the Model
Deep Neural Network
Neural Network Architecture
Hands-On Lab (Tasks)
Step 1: Complete Sprint 1 planning: confirm the goal and select the first backlog tasks
Step 2: Finalize the project dataset and complete a brief EDA in the project notebook.
Step 3: Train a simple baseline model (e.g. logistic/linear regression from Week 3) and record its metric.
Step 4:Commit the baseline notebook to a feature branch and open a draft pull request.
Step 5: In Markdown, state the baseline score every later model must beat
Tools Used
Scikit-learn
Pandas
NumPy
Matplotlib
Jupyter Notebook
Git & GitHub
SMOTE
Learning Outcomes
By the end of the day, I understood the importance of Sprint 1 planning and why a baseline model should be established before developing more complex models. I finalized and analyzed the Heart Disease Health Indicators dataset, inspected its structure, checked for missing values and duplicates, and identified the class imbalance in the target variable. I applied a train/test split and used SMOTE only on the training data to address the class imbalance without introducing data leakage. I then scaled the features and trained a Logistic Regression model as the baseline classifier. The baseline model achieved an Accuracy of 0.745023, Precision of 0.255726, Recall of 0.769766, and F1-score of 0.383912. These results were recorded as the reference point that future Neural Network models should aim to improve upon.

I also learned the fundamental concepts of Neural Networks, including the neuron as a weighted sum plus bias followed by an activation function. I understood the roles of input, hidden, and output layers, as well as the meaning of deep learning and the importance of weights and biases as learnable parameters.

Finally, I established an initial Neural Network architecture for the project that will be implemented and evaluated in the following days.
