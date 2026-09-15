# Week 9 — Day 3: Interactive Streamlit Dashboard

## Overview

This day focused on building a simple and user-friendly **Streamlit dashboard** for the Week 8 melanoma classification model.

The dashboard allows non-technical users to upload a skin-lesion image, run the trained CNN model, and view the prediction with its malignant probability.

## Objectives

* Load the serialized Keras CNN model from the deployment artifacts.
* Apply the same preprocessing used by the FastAPI service.
* Build an interactive image-upload interface using Streamlit.
* Display the prediction clearly as **Benign** or **Malignant**.
* Show the malignant probability and decision threshold.
* Add a probability chart and uploaded-image preview.
* Run the dashboard through Google Colab.

## Model

**Task:** Melanoma Skin Lesion Classification  
**Classes:** Benign / Malignant  
**Input:** 128 × 128 RGB image  
**Preprocessing:** Resize and scale pixel values by 255  
**Selected Threshold:** 0.35  
**Model Format:** Keras `.keras`

## Dashboard Features

* Image uploader for JPG, JPEG, PNG, and WEBP files.
* Adjustable decision threshold.
* Prediction result card.
* Malignant probability metric.
* Probability bar chart.
* Image preview.
* Clean layout suitable for a live project presentation.

## Running the Dashboard

1. Open the Day 3 notebook in Google Colab.
2. Install the required packages.
3. Download or upload the deployment artifacts:

```text
deployment_artifacts/
├── melanoma_cnn.keras
└── model_metadata.json
```

4. Create `/content/app.py` from the notebook.
5. Start Streamlit on port `8503` or another available port.
6. Open the generated Colab link.
7. Upload an image and click **Run prediction**.

## Tools

* Python
* Streamlit
* TensorFlow / Keras
* OpenCV
* NumPy
* Pillow
* Matplotlib
* Google Colab

## Hands-On Lab: Building the Dashboard

- Step 1: Build a Streamlit app that loads the model and takes the project's inputs via appropriate widgets.
- Step 2: Run the model on user input and display the prediction prominently.
- Step 3: Add one supporting visualization (probability, SHAP explanation, or the uploaded image).
- Step 4: Run the app locally and confirm a first-time user can get a prediction easily.
- Step 5: Open a pull request with the deployment code for the mid-sprint Mentor Code Review and address
the feedback.

## Result

The trained CNN was successfully wrapped in an interactive Streamlit dashboard that allows users to upload a skin-lesion image and view the model prediction in a clear and focused interface.
