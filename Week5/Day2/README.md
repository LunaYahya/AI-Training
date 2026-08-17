# Day 2 — DBSCAN & Hierarchical Clustering 
## Learning Objectives
- Describe the drawbacks of K-Means and indicate situations where another clustering algorithm should be used.
- Use DBSCAN to cluster your data and provide an interpretation of the clusters and outliers generated.
- Construct a hierarchical clustering tree (dendrogram) and interpret it.
- Choose between K-Means, DBSCAN, and Hierarchical Clustering.
## Key Topics
- Limitations of K-Means
- DBSCAN: Density-based clustering and noise detection
- Parameters for DBSCAN: eps and min samples
- Hierarchical clustering and Dendrograms
- Appropriate clustering method selection
- Clustering results comparison
## Hands-On Lab(Tasks)
- Step 1: Run DBSCAN on the Day 1 dataset and report how many clusters and noise points it found.
- Step 2: Build a hierarchical clustering dendrogram and choose a cut height, noting the resulting cluster
count.
-  Step 3: Compare the K-Means, DBSCAN, and hierarchical results on the same data.
- step 4: In Markdown, state which method best fits this dataset's shape and why.
## Tools Used
- Scikit-learn (DBSCAN)
- SciPy (linkage, dendrogram)
- Matplotlib
- Jupyter Notebook
- NumPy
- Pandas
## Learning Outcomes
By the end of the day, I gained the understanding of the constraints of K-Means and situations where other clustering algorithms can be used. I got to know that DBSCAN clusters the points in accordance with their density, is capable of detecting clusters of different shapes, and is capable of detecting outliers and noises due to its eps and min_samples parameter values. In addition to this, I gained knowledge about how Hierarchical Clustering creates a hierarchy of clusters and how to read the dendrogram to find the number of clusters.
