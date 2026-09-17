# Technical Write-Up — Melanoma Skin Lesion Classification

## 1. Problem

The project addresses binary image classification of melanoma skin lesions into two categories: Benign and Malignant.

The objective was to develop an end-to-end deep learning workflow that could process skin-lesion images, generate a prediction, evaluate model performance, and expose the trained model through a public Streamlit application.

## 2. Dataset

The project uses a melanoma skin-lesion image dataset containing two classes:

* Benign
* Malignant

The final evaluation used a balanced test set containing 2,000 images, with 1,000 images from each class.

## 3. Methodology

The project followed an end-to-end machine learning pipeline.

Images were processed using OpenCV. The serving contract converts images from BGR to RGB, resizes them to 128 × 128 pixels, converts them to `float32`, and normalizes pixel values by dividing by 255.

A CNN model was trained for binary classification.

The project then evaluated the model using multiple metrics rather than relying only on accuracy. These included precision, recall, F1-score, ROC-AUC, PR-AUC, false positives, and false negatives.

Error analysis was used to understand the types of incorrect predictions.

SHAP was also used to investigate model behavior and provide explainability for image predictions.

Finally, threshold analysis was performed. The reference threshold was 0.50, while 0.35 was selected for deployment.

## 4. Results

At a threshold of 0.50, the model achieved:

* Accuracy: 87.55%
* Malignant precision: 92.43%
* Malignant recall: 81.80%
* Malignant F1-score: 86.79%
* ROC-AUC: 95.17%
* PR-AUC: 94.45%
* False positives: 67
* False negatives: 182

At the selected threshold of 0.35:

* Accuracy: 89.15%
* Malignant precision: 87.46%
* Malignant recall: 91.40%
* Malignant F1-score: 89.39%
* ROC-AUC: 95.17%
* PR-AUC: 94.45%
* False positives: 131
* False negatives: 86

The threshold change increased malignant recall and reduced false negatives while increasing false positives.

ROC-AUC and PR-AUC remained unchanged because the threshold changes the final class decision but not the underlying prediction-score ranking.

## 5. Deployment

The model was packaged with its metadata and deployed through a Streamlit application.

The deployment package contains:

```text
app.py
requirements.txt
README.md
deployment_artifacts/
├── melanoma_cnn.keras
└── model_metadata.json
```

The application uses relative paths so that it can run outside the Colab environment.

The public application was tested and returned an HTTP 200 response.

Live application:

https://ai-training-mipxqexmw7lfuh84hevpb2.streamlit.app/

## 6. Limitations

The model is based on a specific dataset and may not generalize to all real-world populations and image acquisition conditions.

The model can produce both false-positive and false-negative predictions.

The selected threshold changes the precision-recall trade-off but does not eliminate classification errors.

The current application is an educational demonstration and should not be used as a clinical diagnostic system.

## 7. Future Work

Future work could include training on larger and more diverse datasets, evaluating the model on external datasets, exploring additional transfer-learning architectures, improving robustness to image-quality differences, and adding deployment monitoring.

Further work could also investigate approaches for reducing false negatives and improving explainability.

## 8. Conclusion

The project progressed from image-based model development to a complete public deployment.

The final system includes preprocessing, CNN classification, multi-metric evaluation, error analysis, SHAP explainability, threshold analysis, and a public Streamlit interface.

The project is therefore ready for final review and presentation in Week 10.
