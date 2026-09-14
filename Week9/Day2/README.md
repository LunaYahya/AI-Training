# Week 9 — Day 2: Serving the Model with FastAPI

## Overview

This day focused on deploying the validated Week 8 melanoma classification model as a REST API using **FastAPI**.

## Objectives

* Load the trained Keras CNN model.
* Load the deployment metadata and selected threshold.
* Apply the same preprocessing used during training.
* Create a `/predict` endpoint for image classification.
* Validate uploaded files and prediction thresholds.
* Test the API using **Swagger UI**.

## Model

**Task:** Melanoma Skin Lesion Classification
**Classes:** Benign / Malignant
**Input:** 128 × 128 RGB image
**Selected Threshold:** 0.35

## Testing

The API was tested successfully with:

* Health check
* Valid image prediction
* Invalid file type
* Invalid threshold

All expected responses and validation behaviors were confirmed.

## Tools

* Python
* FastAPI
* Uvicorn
* TensorFlow / Keras
* OpenCV
* Pydantic
* Google Colab
* Swagger UI

# Hands-On Lab: Building a Prediction API
- Step 1: Write a FastAPI app that loads the serialized model and preprocessing from Day 1.
- Step 2: Define an input schema with Pydantic matching the project's features.
- Step 3: Implement a /predict endpoint that preprocesses input and returns the prediction as JSON.
- Step 4: Run the server locally and test /predict through the /docs interface with several inputs.
- Step 5: Confirm invalid input is rejected cleanly by Pydantic, documented in the notebook/README.

## Result

The trained CNN was successfully served through a FastAPI REST API and tested through Swagger UI.
