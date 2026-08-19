# Day 4 — t-SNE & Anomaly Detection
## Learning Objectives
- Use t-SNE visualization for high-dimensional datasets and contrast it with PCA.
- Comprehend the t-SNE emphasis on local neighborhood preservation.
- Describe anomaly detection and its nature of being unsupervised.
- Identify anomalies with Isolation Forest method.
- Comprehend the importance of contamination parameter.
- Interpret identified observations marked as anomalies.
- Comprehend the relationship between anomaly detection and clustering like DBSCAN.
## Key Topics
- t-SNE for Visualizing Local Structures
- PCA and t-SNE Comparison
- Local vs. Global Structure
- When to Apply PCA and t-SNE
- What Is Anomaly Detection?
- Unsupervised Anomaly Detection
- Isolation Forest
- Contamination Parameter
- Interpretation of Anomalies Marked by a Model
- Connection between Anomaly Detection and Clustering
- DBSCAN Noise Points as Anomalies
## Hands-On Lab (Tasks)
- Step 1:  Apply t-SNE to reduce a high-dimensional dataset to 2D and plot it, coloring by cluster from Day 1-2.
- Step 2: Compare the t-SNE plot to the PCA plot from Day 3 and note what each reveals.
- Step 3: Run Isolation Forest on the dataset and report how many points were flagged as anomalies.
- Step 4: Inspect two flagged points and hypothesize why they were flagged, documented in Markdown
## Tools Used
- Scikit-learn (TSNE, IsolationForest, PCA, StandardScaler, KMeans)
- Matplotlib
- Jupyter Notebook
- NumPy
- Pandas
## Learning Outcomes
By the end of the day, I understood that t-SNE is one of the algorithms that are used for dimensionality reduction for visualization purposes. Unlike PCA that is used to preserve global variances, t-SNE algorithm preserves the neighborhood structures in high dimensional data.
In addition, I understood what is an anomaly detection and why this problem is considered to be unsupervised. With Isolation Forest, I understood that the way the anomalies were detected was based on the ability of the algorithm to easily isolate these observations.
With Breast Cancer Wisconsin dataset, I applied t-SNE algorithm for visualization of high-dimensional data in two dimensions and compared the results with PCA visualization. Then, I applied the Isolation Forest algorithm with contamination parameter equal to 0.05 and found 29 anomalies among 569 observations.
At last, I checked the features values of two flagged anomalies and compared it with the features values of the whole dataset. Also, I understood that the anomaly detection problem can intersect with clustering problem where noise observations can be considered as anomalies.
