# Day 1 — Sprint 4 Planning, Serialization & MLOps
## Learning Objectives

By the end of this day, we will be able to:

1. Define the Sprint 4 deployment goal and backlog.
2. Document the model and preprocessing contract carried forward from Week 8.
3. Set reproducibility seeds.
4. Save and reload the trained CNN using Keras serialization.
5. Save deployment metadata and environment requirements.
6. Preserve the selected classification threshold.
7. Track model parameters, metrics, and artifacts using MLflow.
8. Create a deployment manifest for the next Sprint 4 tasks.

## Key Topics

- Sprint 4 planning
- Model serialization
- Deployment preprocessing contract
- Training/serving consistency
- Reproducibility and random seeds
- Keras model saving and loading
- Deployment metadata
- Requirements freezing
- MLflow experiment tracking
- Deployment manifest

## Dataset and Project

The notebook prepares a validated CNN trained on the **Melanoma Skin Cancer Dataset — Benign vs Malignant**.

The project contains two image classes:

| Class | Label |
|---|---:|
| Benign | 0 |
| Malignant | 1 |

### Model Configuration

| Configuration | Value |
|---|---|
| Image size | `128 × 128 × 3` |
| Color format | RGB |
| Normalization | Pixel values divided by `255.0` |
| Reference threshold | `0.50` |
| Selected deployment threshold | `0.35` |
| Random seed | `42` |

## Hands-On Lab (Tasks)

- Step 1: Complete Sprint 4 planning and select the deployment backlog tasks.
- Step 2: Serialize the trained model and every preprocessing object (scaler/encoder/vectorizer) to disk.
- Step 3: Write a small script that loads them back and reproduces a known prediction to confirm they work.
- Step 4: Freeze a clean, pinned requirements.txt for the deployment environment.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- OpenCV
- MLflow
- JSON
- Google Colab

## Results

### Deployment Model Contract

| Component | Configuration |
|---|---|
| Model format | Keras `.keras` |
| Input shape | `128 × 128 × 3` |
| Image loading | OpenCV |
| Color conversion | BGR → RGB |
| Normalization | `pixel / 255.0` |
| Class mapping | Benign = 0, Malignant = 1 |
| Selected threshold | `0.35` |
| Random seed | `42` |

### Deployment Artifacts

| Artifact | Description |
|---|---|
| `melanoma_cnn.keras` | Serialized CNN model |
| `model_metadata.json` | Model and preprocessing configuration |
| `requirements.txt` | Required deployment packages |
| `deployment_manifest.json` | Complete deployment package description |

### Week 8 Metrics at the Selected Threshold

| Metric | Result |
|---|---:|
| Accuracy | 0.8915 |
| Precision — Malignant | 0.8746 |
| Recall — Malignant | 0.9140 |
| F1-score — Malignant | 0.8939 |
| ROC-AUC | 0.9517 |
| PR-AUC | 0.9445 |
| False positives | 131 |
| False negatives | 86 |


## Learning Outcomes

At the end of the day, I was able to define the Sprint 4 deployment plan, package the validated Week 8 CNN, document its preprocessing contract, save the deployment metadata and environment requirements, and create a deployment manifest.

I also used MLflow to make the model and its configuration traceable and ready for integration into a prediction API or user-facing application.

