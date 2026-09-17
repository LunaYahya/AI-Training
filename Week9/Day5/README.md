# Melanoma Skin Lesion Classification

## Overview

This project develops a deep learning image classification system for identifying melanoma skin lesions as either **Benign** or **Malignant**.

The project covers the complete machine learning lifecycle, from image preprocessing and CNN model development to evaluation, explainability, and public deployment using Streamlit.


## Problem Statement

Melanoma is a serious form of skin cancer, and image-based classification can be used as a machine learning research problem to distinguish benign and malignant skin lesions.

The goal of this project is to build an image classification model that receives a skin-lesion image and predicts:

* Benign
* Malignant

The deployed application also returns a malignant probability and applies a selected classification threshold.

## Dataset

The project uses a melanoma skin-lesion image dataset containing two classes:

* Benign
* Malignant

The evaluation stage used a balanced test set of 2,000 images:

* 1,000 Benign
* 1,000 Malignant

## Methodology

The project follows an end-to-end image classification pipeline:

```text
Dataset
   ↓
Image Preprocessing
   ↓
Image Resizing
   ↓
Normalization
   ↓
Data Augmentation
   ↓
CNN Model
   ↓
Training
   ↓
Evaluation
   ↓
Error Analysis
   ↓
SHAP Explainability
   ↓
Threshold Analysis
   ↓
Streamlit Deployment
```

### Preprocessing

The deployment preprocessing contract is:

* Image decoding using OpenCV
* BGR to RGB conversion
* Resize to 128 × 128
* Convert to `float32`
* Normalize pixel values by dividing by 255.0

### Model

The trained model is stored as:

```text
melanoma_cnn.keras
```

Model metadata is stored in:

```text
model_metadata.json
```

The reproducibility seed is:

```text
42
```

## Classification Threshold

The reference threshold was 0.50.

After threshold analysis, the selected deployment threshold was:

```text
0.35
```

The decision rule is:

```text
malignant probability >= 0.35 → Malignant
malignant probability < 0.35 → Benign
```

The threshold was selected to increase malignant recall and reduce false negatives compared with the 0.50 reference threshold.

## Results

At the reference threshold of 0.50:

| Metric              | Result |
| ------------------- | -----: |
| Accuracy            | 87.55% |
| Malignant Precision | 92.43% |
| Malignant Recall    | 81.80% |
| Malignant F1-score  | 86.79% |
| ROC-AUC             | 95.17% |
| PR-AUC              | 94.45% |
| False Positives     |     67 |
| False Negatives     |    182 |

At the selected threshold of 0.35:

| Metric              | Result |
| ------------------- | -----: |
| Accuracy            | 89.15% |
| Malignant Precision | 87.46% |
| Malignant Recall    | 91.40% |
| Malignant F1-score  | 89.39% |
| ROC-AUC             | 95.17% |
| PR-AUC              | 94.45% |
| False Positives     |    131 |
| False Negatives     |     86 |

The threshold change demonstrates the precision-recall trade-off. The selected threshold produces higher malignant recall and fewer false negatives, while producing more false positives.

## Explainability

SHAP was used during the project to investigate model behavior and provide visual explanations of image predictions.

Explainability is included as an analysis tool and does not guarantee that the model's reasoning is medically valid.

## Deployment

The final application is deployed using Streamlit.

### Deployment package

```text
app.py
requirements.txt
README.md
deployment_artifacts/
├── melanoma_cnn.keras
└── model_metadata.json
```

The application uses deployment-safe relative paths instead of Colab-specific paths.

## Live Demo

**Public Application:**

https://ai-training-mipxqexmw7lfuh84hevpb2.streamlit.app/

## Run Locally

Clone the repository and navigate to the deployment directory.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Reproducibility

The project documents the model-serving contract, preprocessing steps, model artifact, dependency versions, and random seed.

The deployment environment should use the pinned versions in `requirements.txt`.

## Limitations

The model was developed using a specific image dataset and therefore may not generalize to every real-world population or imaging condition.

The model can produce both false-positive and false-negative predictions.

The classification threshold affects the balance between these errors.

The current system is an educational machine learning demonstration and is not intended for clinical diagnosis.

## Future Work

Future improvements may include:

* Larger and more diverse datasets
* External dataset validation
* Additional CNN and transfer-learning architectures
* Improved robustness to image-quality differences
* More systematic hyperparameter tuning
* Deployment monitoring
* Extended explainability analysis
* Further investigation of methods for reducing important false negatives

## Project Status

The project has completed the Phase 3 development and deployment workflow and is prepared for the Week 10 final presentation, portfolio review, and certification stage.
