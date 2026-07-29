## Day 4 – EDA Part 1: Distributions & Outliers

On the fourth day, we learned about Exploratory Data Analysis (EDA), which is the first and most important step before building any machine learning model. EDA helps us understand the structure of a dataset, identify patterns, detect outliers, and discover potential data quality issues before training a model.

## Learning Objectives

we learned why EDA is essential before modeling and how to perform univariate analysis using different statistical visualizations. We used Seaborn to create histograms, box plots, count plots, and KDE plots to understand data distributions. We also learned how to detect outliers using the Interquartile Range (IQR) method and decide the appropriate way to handle them.

## Key Concepts
Why EDA is Important for Machine Learning?
EDA helps identify patterns, understand feature distributions, detect missing values and outliers, and improve data quality before applying machine learning algorithms.
Univariate Analysis: It analyzes one variable at a time to understand its distribution and characteristics.
Histogram: Displays the distribution of numerical data and helps identify the shape of the data.
Box Plot: Shows the median, quartiles, spread of the data, and highlights potential outliers.
Count Plot: Displays the frequency of each category in a categorical feature.
KDE Plot: Provides a smooth estimate of the distribution of a numerical variable.
IQR Method: A statistical technique used to detect potential outliers by identifying values outside the range of Q1 − 1.5 × IQR and Q3 + 1.5 × IQR.
## Tools Used
- Python
- Pandas
- Seaborn
- Matplotlib
- Jupyter Notebook
- Git & GitHub
## Hands-On Lab (Tasks)
- Step 1: Load a provided real dataset and produce a histogram for each numeric variable.
- Step 2: Produce a box plot for the key numeric variables and identify any outliers visually.
- Step 3: Apply the IQR method in code to flag outliers in at least one column, and decide (with justification)
how to handle them.
- Step 4: Produce a count plot for each categorical variable and note any class imbalance.
- Step 5: Document what each distribution reveals in Markdown cells
## Learning Outcomes
The learning outcome of doing this day is acquiring hands-on experience in conducting exploratory data analysis prior to machine learning. This  taught me how to conduct analysis of distributions of data using various types of visualization, identify outliers using the IQR technique, and describe the features of numerical and categorical variables.
