# Day 5 — Full Evaluation, Explainability & Sprint Review

## Learning Objectives

- Evaluate the Melanoma image-classification model using task-appropriate metrics, including Accuracy, Precision, Recall, F1-score, ROC-AUC, and PR-AUC.
- Understand why accuracy alone is not sufficient when false negatives are important.
- Analyze the precision–recall trade-off by evaluating multiple classification thresholds.
- Select a candidate operating threshold according to the project's priorities.
- Identify false positives and false negatives using the untouched test set.
- Use SHAP to generate a local explanation for an individual prediction.
- Generate a small global-style SHAP analysis showing influential image regions.
- Complete the Sprint 3 Review and Retrospective.
- Define a concrete Sprint 4 action focused on deployment and final polish.

## Key Topics

- Full task-appropriate model evaluation
- Precision, Recall, and F1-score
- ROC-AUC and PR-AUC
- Confusion matrix
- False positives and false negatives
- Precision–recall trade-off
- Threshold tuning
- SHAP explainability for image models
- Local and global-style explanations
- Sprint Review and Retrospective
- Deployment planning

## Dataset

The notebook uses the **Melanoma Skin Cancer Dataset — Benign vs Malignant**. The images are organized into separate `train/` and `test/` directories with two classes: `Benign` and `Malignant`.

| Dataset Split | Number of Images | Classes |
|---|---:|---:|
| Training data | 11,879 | 2 |
| Training subset | 9,503 | 2 |
| Validation subset | 2,376 | 2 |
| Test set | 2,000 | 2 |

The class mapping is:

| Class | Label |
|---|---:|
| Benign | 0 |
| Malignant | 1 |

The test set contains 1,000 Benign images and 1,000 Malignant images.

## Hands-On Lab (Tasks)
- Step 1: Produce the full evaluation for the project with the correct metrics, reported against the Week 6
baseline.
- Step 2: If the task is imbalanced, apply SMOTE or threshold tuning and report the precision-recall tradeoff.
- Step 3: Generate SHAP global feature importance and at least one per-prediction explanation.
- Step 4: Ensure all Sprint 3 work is committed, the pull request is merged after mentor approval, and
results are documented.
- Step 5: Present the Sprint Review, then write the Retrospective with one concrete change for Sprint 4
(deployment).
## Tools Used

- Python
- TensorFlow / Keras
- SHAP
- OpenCV
- Scikit-learn
- Seaborn
- Matplotlib
- NumPy
- Pandas
- KaggleHub
- Google Colab
- Git / GitHub

## Results

### Shared Image Preprocessing

| Preprocessing Step | Configuration |
|---|---|
| Image loading | OpenCV `cv2.imread()` |
| Color conversion | BGR → RGB |
| Image size | 128 × 128 × 3 |
| Data type | `float32` |
| Pixel normalization | Divide by 255.0 |
| Shared function | `preprocess_image()` |

The same preprocessing logic is used for training, validation, testing, and SHAP explanations. This helps prevent differences between the training and prediction pipelines.

### CNN Training

| Training Configuration | Value |
|---|---:|
| Image size | 128 × 128 × 3 |
| Batch size | 32 |
| Number of epochs | 5 |
| Training images | 11,879 |
| Training subset | 9,503 |
| Validation images | 2,376 |
| Model output | Malignant probability |
| Initial/reference threshold | 0.50 |
| Selected candidate threshold | 0.35 |

The CNN architecture contains two convolutional blocks followed by a Flatten layer, a Dense layer with 128 units, Dropout with a rate of 0.3, and a sigmoid output representing the probability of the Malignant class.

### Reference Threshold Evaluation

At the reference threshold of 0.50, the model achieved the following results:

| Metric | Result |
|---|---:|
| Accuracy | 0.8755 |
| Precision — Malignant | 0.9243 |
| Recall — Malignant | 0.8180 |
| F1-score — Malignant | 0.8679 |
| ROC-AUC | Reported in notebook |
| PR-AUC | Reported in notebook |
| False positives | 67 |
| False negatives | 182 |

### Classification Report at the Reference Threshold

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Benign | 0.8368 | 0.9330 | 0.8823 | 1,000 |
| Malignant | 0.9243 | 0.8180 | 0.8679 | 1,000 |
| Macro average | 0.8805 | 0.8755 | 0.8751 | 2,000 |
| Weighted average | 0.8805 | 0.8755 | 0.8751 | 2,000 |

### Threshold Tuning

Several thresholds between 0.20 and 0.80 were evaluated. The candidate threshold with the highest F1-score was 0.35.

| Operating Point | Threshold | Precision — Malignant | Recall — Malignant | F1-score — Malignant | False Positives | False Negatives |
|---|---:|---:|---:|---:|---:|---:|
| Reference Threshold | 0.50 | 0.9243 | 0.8180 | 0.8679 | 67 | 182 |
| Selected Threshold | 0.35 | 0.8746 | 0.9140 | 0.8939 | 131 | 86 |

The selected threshold increases Malignant recall and reduces false negatives. This comes with a decrease in precision and an increase in false positives. The threshold is therefore a transparent candidate operating point rather than a final clinical decision rule.

### Confusion Matrix and Error Analysis

At the reference threshold of 0.50:

| Error Measure | Count | Meaning |
|---|---:|---|
| True negatives | 933 | Benign images correctly predicted as Benign |
| False positives | 67 | Benign images incorrectly predicted as Malignant |
| False negatives | 182 | Malignant images incorrectly predicted as Benign |
| True positives | 818 | Malignant images correctly predicted as Malignant |

At the selected threshold of 0.35, the final error analysis identified 131 False Positives and 86 False Negatives. False Negatives receive special attention because they represent Malignant images predicted as Benign.

The visual inspection of misclassified examples considers possible visual similarity between classes, image quality, lighting and background variation, lesion appearance, and limitations of the current CNN. These observations are qualitative and do not establish a medical cause for a prediction error.

### SHAP Explainability

SHAP `GradientExplainer` was created using a small background sample of 8 training images. A local explanation was generated for a False Negative with the following characteristics:

| Explanation Item | Value |
|---|---|
| Actual class | Malignant |
| Predicted class | Benign |
| Malignant probability | 0.0579 |
| SHAP output shape | 128 × 128 × 3 |

The local explanation overlays SHAP contribution magnitude on the input image to show which image regions influenced the model output. A global-style SHAP map was also generated from a small sample of 3 test images. Because the sample is intentionally small for computational practicality, the global-style map should be interpreted as exploratory rather than as a definitive global feature-importance result.

## Learning Outcomes

At the end of Day 5, I was able to evaluate an image-classification model using task-appropriate metrics, analyze false positives and false negatives, tune the classification threshold, and explain predictions with SHAP. I also completed the Sprint 3 Review and Retrospective, documented the model's limitations, saved the metrics independently, and defined deployment and final-polish work for Sprint 4.
