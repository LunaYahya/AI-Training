# Day 1 — Unsupervised Learning & K-Means
## Learning Objectives
- Learn how supervised and unsupervised learning differ from each other.
- Learn what clustering is and how it groups the observations together.
- Apply the K-Means clustering technique.
- Learn about cluster centroids and the method through which K-Means divides the data into clusters.
- Determine the optimal number of clusters using the Elbow Method and Silhouette Score.
- Learn why scaling features is essential before applying K-Means clustering.
## Dataset Used
For K-Means clustering, the **Credit Card Fraud Detection** dataset was used.
The dataset had numerical variables which were standardized prior to the clustering process. The Class variable was not considered as an input feature since K-Means is an unsupervised learning technique and does not need target variables.
## What I Have Learned
- The difference between **supervised and unsupervised learning**.
- Clustering as a way of identifying natural groups in the data based on distances without labeled data.
- The working mechanism of the **K-Means** clustering algorithm including observation assignment to the closest cluster centroid and the update of centroids.
- Cluster centroids.
- The importance of feature scaling for distance-based algorithms like K-Means.
- How **Elbow Method** uses the inertia value to find a proper number of clusters.
- What the **Silhouette Score** is and how it measures the quality of clusters and separation of clusters from each other.
- The selection of a good candidate k value among several candidate values using the Silhouette Score.
## Hands-On-Lab(Tasks)
- Step 1: Load and scale a provided dataset (numeric features only) with StandardScaler.
- Step 2: Run K-Means for k from 1 to 10 and plot inertia to find the elbow.
- Step 3: Compute the silhouette score for the top two candidate k values and pick the best.
- Step 4: Fit final K-Means with the chosen k, and visualize the clusters on a 2D scatter plot.
- Step 5: Interpret what each cluster represents in a Markdown cell.
## Tools Used
- Python
- Pandas
- NumPy
- Scikit-learn( KMeans,StandardScaler,silhouette_score,train_test_split)
- Matplotlib
- Jupyter Notebook
## Key Outcome
By the end of Day 1, I successfully applied **unsupervised learning with K-Means clustering** to identify clusters in numeric data. I gained an understanding of feature scaling before performing the clustering, applying the Elbow and Silhouette scores to determine the number of clusters, and interpreting clusters and their centroids.
> **Note:** The creditcard.csv dataset is not included in this repository because its file size exceeds GitHub's 100 MB file size limit. The dataset was used locally for analysis and model development and can be downloaded from Kaggle.
