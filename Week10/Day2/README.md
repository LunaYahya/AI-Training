#  Melanoma Skin Lesion Classification

A Deep learning application for classifying skin lesion images as **Benign** or **Malignant**.

This project covers an end-to-end machine learning workflow, including image preprocessing, deep learning, model evaluation, prediction, and deployment using Streamlit.


---

##  Live Demo

🔗 **Streamlit App:** **[https://ai-training-mipxqexmw7lfuh84hevpb2.streamlit.app/]**

---

##  Project Overview

Melanoma is a serious form of skin cancer, and image classification can be used as a machine learning approach for analyzing skin lesion images.

The goal of this project is to build a deep learning model that classifies skin lesion images into two categories:

* **Benign**
* **Malignant**

The final model was integrated into a **Streamlit web application**, allowing users to upload an image and receive:

* The predicted class
* The malignant probability
* A classification result based on a selected threshold

---

##  Objectives

The main objectives of this project were to:

* Build an image classification model for skin lesion images.
* Develop an image preprocessing pipeline.
* Train and evaluate a deep learning model.
* Analyze model performance using multiple classification metrics.
* Build a reusable prediction function.
* Apply probability-based classification and threshold tuning.
* Integrate the trained model into a Streamlit application.
* Deploy the model as an interactive web application.

---

##  Dataset

The project uses a Kaggle dataset containing images divided into two classes:

| Class     | Number of Images |
| --------- | ---------------: |
| Benign    |           1,000 |
| Malignant |            1,000|
| **Total** |       **2,000 ** |

The images were prepared for deep learning using a standardized input size of:

```text
128 × 128 × 3
```

The three channels represent RGB color information.

---

##  Machine Learning Workflow

The complete workflow can be summarized as:

Skin Lesion Dataset --> Image Loading --> Image Preprocessing --> Resize to 128 × 128 --> RGB Conversion--> Normalization -->Deep Learning Model --> Model Evaluation --> Prediction Function--> Probability + Threshold --> Streamlit Application


---

## Image Preprocessing

The input images are processed before being passed to the model.

The preprocessing workflow includes:

### Image Resizing

All images are resized to:

```text
128 × 128 pixels
```

This ensures that all model inputs have the same dimensions.

### RGB Conversion

Images are converted to the required RGB format when necessary.

### Normalization

Pixel values are normalized before model inference to maintain consistent input values.

### Data Augmentation

Augmentation techniques can be applied during training to introduce variation into the training images and improve model generalization.

---

##  Deep Learning Model

The project uses **TensorFlow/Keras** for deep learning-based image classification.

The model receives a preprocessed image and produces a probability representing how likely the image is to belong to the malignant class.

The prediction process is:

text
Input Image -->
Preprocessing -->Deep Learning Model -->Malignant Probability -->Classification Threshold -->Benign / Malignant


---

## Prediction Pipeline

A reusable prediction function was developed to connect preprocessing, model inference, and prediction output.

The prediction function accepts an image path and returns:

* Class ID
* Class name
* Malignant probability

Example:

```python
predict(image_path, threshold=0.5)
```

Example output:

```text
Class: Malignant
Malignant Probability: 0.93
```

This approach allows the same prediction workflow to be reused by the deployed application.

---

## Model Evaluation

The model was evaluated using multiple metrics rather than relying on accuracy alone.

The main metrics include:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Why These Metrics Matter

For a binary classification problem such as this one, accuracy alone may not fully describe the model's behavior.

Particular attention was given to **false negatives**, where a malignant image is incorrectly classified as benign.

The project therefore considers precision, recall, F1-score, and confusion-matrix results when evaluating the model.

---

##  Threshold Tuning

The model produces a probability rather than directly returning a class.

For example:

```text
Malignant Probability = 59.3%
```

A classification threshold determines how this probability is converted into the final class.

The project explored threshold-based prediction to better understand the trade-off between false positives and false negatives.

This makes the prediction pipeline more flexible than using a fixed class output alone.

---

##  Example Predictions

The deployed application was tested using different images.

###  Example 1 — Benign

```text
Prediction: Benign
Malignant Probability: 22.7%
```

The model correctly classified the example as benign.

### Example 2 — Malignant

```text
Prediction: Malignant
Malignant Probability: 100%
```

The model correctly classified the example as malignant.

###  Example 3 — Malignant

```text
Prediction: Malignant
Malignant Probability: 59.3%
```

This example demonstrates why the probability and classification threshold are both important when interpreting predictions.

---

##  Deployment

The trained model was integrated into a **Streamlit** application.

The application allows a user to:

1. Upload a skin lesion image.
2. Preprocess the image.
3. Run model inference.
4. Calculate the malignant probability.
5. Apply the selected classification threshold.
6. Display the prediction.

### Application Workflow

```text
Upload Image
      ↓
Preprocess Image
      ↓
Load Model
      ↓
Run Inference
      ↓
Calculate Probability
      ↓
Apply Threshold
      ↓
Display Prediction
```

---

##  Technologies Used

### Programming & Data

* Python
* NumPy
* Pandas

### Machine Learning & Deep Learning

* TensorFlow
* Keras
* Scikit-learn

### Computer Vision

* OpenCV

### Visualization & Evaluation

* Matplotlib
* Seaborn
* Confusion Matrix
* Precision
* Recall
* F1-score

### Deployment

* Streamlit

### Development & Version Control

* Jupyter Notebook
* Google Colab
* VS Code
* Git
* GitHub

---


##  Installation

Clone the repository:

```bash
git clone https://github.com/LunaYahya/AI-Training.git
```

Move to the project directory:

```bash
cd AI-Training
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```


---

##  Run the Application

Navigate to the folder containing the final `app.py` and run:

```bash
streamlit run app.py
```

The application will open in the browser and allow an image to be uploaded for prediction.

---

## Final Results

The final evaluation results of the deployed model are:

| Metric    |                 Result |
| --------- | ---------------------: |
| Accuracy  | **[89.15%]** |
| Precision | **[87.46%]** |
| Recall    | **[91.40%]** |
| F1-Score  | **[89.39%]** |
| ROC-AUC   | **[95.17%]** |


---

## Key Challenges & Lessons Learned

### 1. Building an End-to-End Pipeline

The project required connecting multiple stages instead of working only inside a notebook:


Preprocessing → Model → Prediction → Application


### 2. Consistent Preprocessing

Using the same preprocessing logic during training and inference helps reduce the risk of training-serving skew.

### 3. Evaluation Beyond Accuracy

The project demonstrated why precision, recall, F1-score, and confusion matrices are important when evaluating classification models.

### 4. False Negatives

The project highlighted the importance of analyzing false negatives instead of focusing only on overall accuracy.

### 5. Deployment

Deploying the model through Streamlit transformed the project from a notebook-based experiment into an interactive application.

---

##  Future Improvements

Possible future improvements include:

* Testing transfer-learning architectures such as MobileNetV2 and EfficientNet.
* Further tuning the classification threshold.
* Applying class weighting when needed.
* Improving model generalization with additional data.
* Adding Grad-CAM or SHAP-based explanations.
* Improving the Streamlit user interface.
* Adding MLflow experiment tracking.
* Adding automated tests for the prediction pipeline.
* Monitoring model performance after deployment.

---

## Project Context

This project was developed as the final capstone project during an **AI and Machine Learning training program**.

It combines skills developed throughout the training, including:

* Python
* Data preprocessing
* Machine learning
* Deep learning
* Computer vision
* Model evaluation
* Prediction pipelines
* Model deployment

The project demonstrates the complete workflow from raw image data to a deployed machine learning application.

---



## 🔗 Project Links

* **GitHub Repository:** https://github.com/LunaYahya/AI-Training
* **Week 9:** https://github.com/LunaYahya/AI-Training/tree/main/Week9
* **Live Demo:** **[https://ai-training-mipxqexmw7lfuh84hevpb2.streamlit.app/]**




