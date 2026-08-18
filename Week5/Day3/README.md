# Day 3 — Dimensionality Reduction with PCA
## Learning Objectives
- Explain the curse of dimensionality and why dimensionality reduction is useful.
- Perform PCA to reduce the dimensionality of a data set.
- Learn about principal components and variance capturing.
- Learn about the explained variance and selecting the right number of components.
- Learn when to use and when not to use PCA.
##  Key Topics
- The Curse of Dimensionality
- Principal Component Analysis (PCA)
- Principal Components & Variance
- Ratio of Variance explained
- Cumulative Variance explained
- Selection of the number of components based on 95% Variance
- Dimensionality Reduction & Visualizing in 2 Dimensions
- Benefits & Drawbacks of PCA
- Interpretability problem with PCA
## Hands-On Lab(Tasks)
- Step 1: Scale a high-dimensional provided dataset with StandardScaler.
- Step 2: Fit PCA and plot the cumulative explained variance against the number of components.
- Step 3: Choose the number of components that retains ~95% of the variance and justify it.
- Step 4: Reduce the data to 2 components and produce a 2D scatter plot, coloring points by a known group
if available.
- Step 5: Document what the reduction preserved and what it cost in Markdown
## Tools Used
- Scikit-learn (PCA, StandardScaler)
- Matplotlib
- Jupyter Notebook
- NumPy
- Pandas
## Learning Outcomes
By the end of the day, I got familiarized with the idea of the curse of dimensionality and how it is possible to reduce the dimensions of the data in order to make it more manageable. I got familiar with the concept of how PCA constructs new principal components that capture the variance of the data in the directions where it varies the most. In addition to that, I learned about using the explained variance and cumulative explained variance to find out how many components to use. Working with the Breast Cancer Wisconsin dataset, I reduced the number of features from 30 to 10 principal components while preserving around 95.16% of the variance.
