# Week 8 — Data Processing and Model Evaluation

Week 8 focuses on preparing text and image data, converting it into suitable model representations, building end-to-end prediction pipelines, and evaluating, analyzing, and explaining machine-learning models as part of **Sprint 3**.

## Learning Objectives

- Apply preprocessing techniques to text and image data.
- Compare traditional and modern text representations.
- Build a complete image-classification prediction pipeline.
- Evaluate models using task-appropriate metrics instead of accuracy alone.
- Analyze errors, tune classification thresholds, and explain predictions with SHAP.
- Document Sprint 3 results and define the next steps for Sprint 4.

## Daily Topics

| Day | Topic | Main Activities |
|---|---|---|
| [Day 1](./Day1) | Sprint 3 Planning & NLP Preprocessing | Tokenization, cleaning, lemmatization, and preserving sentiment-critical negations |
| [Day 2](./Day2) |Text Representation: TF-IDF & Embeddings | Bag-of-Words, TF-IDF, GloVe, and contextual DistilBERT representations |
| [Day 3](./Day3) |  Computer Vision Preprocessing with OpenCV | OpenCV, resizing, BGR-to-RGB conversion, normalization, augmentation, and Canny edge detection |
| [Day 4](./Day4) | Model Integration & Error Analysis | Reusable `predict()` function, confusion matrix, precision/recall, and misclassified-image analysis |
| [Day 5](./Day5) | Full Evaluation, Explainability & Sprint Review | ROC-AUC, PR-AUC, threshold tuning, SHAP, and Sprint 3 review |

## Projects and Datasets

- **Text dataset:** Google Play Store reviews for sentiment classification.
- **Image dataset:** Melanoma skin-cancer images with two classes: `Benign` and `Malignant`.
- **Main tools:** Python, NLTK, Transformers, GloVe, OpenCV, TensorFlow/Keras, Scikit-learn, SHAP, Matplotlib, Seaborn, KaggleHub, and Google Colab.

## Key Results

- **TF-IDF + Logistic Regression** achieved approximately **89.8% accuracy**, making it a strong traditional baseline.
- **DistilBERT** remained the preferred representation for capturing context and semantic relationships in text.
- A shared image-preprocessing pipeline was used consistently during training, testing, and prediction to prevent training/serving skew.
- For the image model, lowering the classification threshold from `0.50` to `0.35` increased malignant recall from `0.818` to `0.914` and reduced false negatives from `182` to `86`, while increasing false positives.
- SHAP was used to explain the image regions influencing selected model predictions.


## How to Run

Each day includes a notebook named `Day*_note.ipynb`. The notebooks can be run in **Google Colab** after downloading the required datasets and installing the dependencies.

```bash
pip install numpy pandas matplotlib seaborn scikit-learn opencv-python tensorflow shap nltk transformers gensim kagglehub
```

## Deliverables

- A Jupyter notebook for each training day.
- Reusable preprocessing pipelines for text and image data.
- Evaluation reports, confusion matrices, and error analyses.
- SHAP-based prediction explanations.
- Documentation of preprocessing decisions, Sprint 3 results, and the next action plan.

## Next Step

Move to **Sprint 4**, focusing on deployment, model improvements, and final project polishing.

---

For more details, visit [Day 1](./Day1), [Day 2](./Day2), [Day 3](./Day3), [Day 4](./Day4), and [Day 5](./Day5).
