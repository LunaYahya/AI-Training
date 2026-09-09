# Day 4 — Model Integration & Error Analysis

## Learning Objectives

- Integrate image preprocessing and a trained CNN model into one end-to-end prediction pipeline.

- Use the same preprocessing function during training, testing, and prediction to prevent training/serving skew.

- Build a reusable `predict()` function that accepts a raw image path and returns a predicted class and malignant probability.

- Evaluate the model using accuracy, a classification report, and a confusion matrix.

- Identify the most common error type by comparing false positives and false negatives.

- Inspect misclassified images and categorize them as possible model weaknesses or data-quality issues.

- Document findings and propose practical improvements for the model.

## Key Topics

- End-to-end model integration

- Shared image preprocessing

- Training/serving skew

- Raw image prediction

- Confusion matrix

- False positives and false negatives

- Classification report

- Misclassified image inspection

- Qualitative error analysis

- Threshold-based classification

## Dataset

The notebook uses the Melanoma Skin Cancer Dataset — Benign vs Malignant. The dataset contains two image classes: `Benign` and `Malignant`, organized into separate `train/` and `test/` directories.

The notebook detected the following image counts:

| Dataset Split | Number of Images | Classes |
|---|---:|---:|
| Training subset | 11,879 | 2 |
| Validation subset | 2,376 | 2 |
| Test set | 2,000 | 2 |

The model uses the following class mapping:

| Class | Label |
|---|---:|
| Benign | 0 |
| Malignant | 1 |

## Hands-On Lab (Tasks)

- Step 1: Wrap the project's preprocessing and model into a single predict() function taking raw input to a prediction.

- Step 2: Verify prediction-time preprocessing exactly matches training-time preprocessing.

- Step 3: Produce a confusion matrix and identify the model's most common error type.

- Step 4: Pull out at least three misclassified examples, read them, and categorize each as a data issue or a model weakness in Markdown.


## Tools Used

- OpenCV

- TensorFlow/Keras

- Scikit-learn

- Seaborn

- Matplotlib

- NumPy

- Pandas

- KaggleHub

- Google Colab

## Results

Shared Preprocessing Pipeline

| Preprocessing Step | Configuration |
|---|---|
| Image loading | OpenCV `cv2.imread()` |
| Color conversion | BGR → RGB |
| Image size | 128 × 128 × 3 |
| Data type | `float32` |
| Pixel normalization | Divide by 255.0 |
| Shared function | `preprocess_image()` |

The same `preprocess_image()` function is used to build the training data, build the test data, and prepare raw images passed to `predict()`. This prevents differences between the training and serving pipelines.

CNN Training

| Training Configuration | Value |
|---|---:|
| Image size | 128 × 128 × 3 |
| Batch size | 32 |
| Number of epochs | 5 |
| Training samples | 11,879 |
| Validation fraction | 20% |
| Output type | Malignant probability |
| Classification threshold | 0.50 |

Test Evaluation

| Metric | Result |
|---|---:|
| Test loss | 0.5046 |
| Test accuracy | 0.7685 |
| Total test predictions | 2,000 |
| Total misclassified images | 463 |

Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Benign | 0.6898 | 0.9760 | 0.8083 | 1,000 |
| Malignant | 0.9590 | 0.5610 | 0.7079 | 1,000 |
| Macro average | 0.8244 | 0.7685 | 0.7581 | 2,000 |
| Weighted average | 0.8244 | 0.7685 | 0.7581 | 2,000 |

Confusion Matrix and Error Analysis

| Error Measure | Count | Meaning |
|---|---:|---|
| True negatives | 976 | Benign images correctly predicted as Benign |
| False positives | 24 | Benign images incorrectly predicted as Malignant |
| False negatives | 439 | Malignant images incorrectly predicted as Benign |
| True positives | 561 | Malignant images correctly predicted as Malignant |

## Learning Outcomes

At the end of the day, I was able to build an end-to-end machine-learning workflow connecting preprocessing, model inference, and prediction. I used shared preprocessing for training, testing, and raw-image prediction, created a reusable `predict()` function, and evaluated the model using a classification report and confusion matrix. I also analyzed misclassified images, identified false negatives as the main error, and suggested improvements such as transfer learning, augmentation, class weighting, threshold tuning, and ROC-AUC or PR-AUC evaluation.


