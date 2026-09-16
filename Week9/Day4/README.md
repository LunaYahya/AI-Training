# Week 9 — Day 4: Public Deployment

## Melanoma Skin Lesion Classification — Benign vs Malignant

This project deploys the Streamlit dashboard developed in **Week 9 — Day 3** as a public web application. The dashboard loads a serialized Keras convolutional neural network, applies the project preprocessing contract, and displays a prediction with the malignant probability.


## Live Application

The deployed application is available at:

**[Open the Melanoma Classifier](https://ai-training-mipxqexmw7lfuh84hevpb2.streamlit.app/)**

The application is hosted with **Streamlit Community Cloud** and connected to the GitHub repository.

## Notebook

The complete Google Colab workflow is available in [`Day4_note.ipynb`](./Day4_note.ipynb). It continues from Day 3 and covers deployment preparation, dependency management, artifact validation, local testing, and live deployment testing.

## Learning Objectives

This day focuses on moving a machine-learning application from a local or Colab environment to a public URL. The notebook explains why a deployment needs an explicit dependency file, how to package the application and model artifacts, how to use deployment-safe relative paths, and how to compare local and deployed predictions.

By completing the notebook, learners can:

- Prepare a Streamlit application for public hosting.
- Create a reproducible `requirements.txt` file.
- Package a serialized `.keras` model and its metadata.
- Separate temporary Colab paths from portable application paths.
- Deploy an application with Streamlit Community Cloud.
- Test the live application with multiple image formats and inputs.
- Investigate differences between local and deployed predictions.

## Model and Preprocessing Contract

The deployed application preserves the serving contract established in the earlier sprint work.

| Component | Specification |
|---|---|
| Project | Melanoma skin cancer classification |
| Classes | Benign and Malignant |
| Model format | Keras `.keras` |
| Model artifact | `melanoma_cnn.keras` |
| Input shape | `128 × 128 × 3` |
| Color format | RGB |
| Image reader | Pillow in the deployed Streamlit app |
| Resize | `128 × 128` |
| Data type | `float32` |
| Normalization | Pixel values divided by `255.0` |
| Positive class | Malignant |
| Selected threshold | `0.35` |

A probability greater than or equal to `0.35` is classified as **Malignant**. Otherwise, the prediction is **Benign**.


## Dependencies

The deployed application uses a Python 3.12 runtime and the following packages:

```text
streamlit==1.36.0
tensorflow==2.19.0
numpy==1.26.4
pillow==10.4.0
```

`runtime.txt` contains:

```text
python-3.12
```

Pillow is used for image loading and preprocessing in the deployed application. This avoids platform-specific OpenCV import problems on Streamlit Community Cloud.

## Deployment Workflow

The deployment process is:

1. Prepare `app.py` with relative artifact paths.
2. Add the serialized model and `model_metadata.json` to `deployment_artifacts/`.
3. Add `requirements.txt` and `runtime.txt` to the same directory as `app.py`.
4. Commit the files to the GitHub repository.
5. Create a new application in [Streamlit Community Cloud](https://share.streamlit.io/).
6. Select the repository, branch, and `Week9/Day4/app.py` as the main file.
7. Wait for dependency installation and application startup.
8. Open the public URL and test image uploads and predictions.

## Testing the Live App

The live application should be tested as a real user would use it. The test procedure includes uploading JPG and PNG images, running a prediction, reviewing the malignant probability, and changing the decision threshold. The application should also provide a clear response when an invalid or unreadable file is uploaded.

For prediction parity, use the same image bytes in the local and deployed environments. Compare both the predicted class and the malignant probability. A substantial difference usually indicates a mismatch in the model artifact, metadata, preprocessing steps, dependency versions, or file paths.


## Result

The melanoma classification dashboard was successfully deployed as a public Streamlit application. Users can open the live URL, upload a skin-lesion image, and view the model prediction and malignant probability through an interactive interface.


