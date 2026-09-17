# Full Project Retrospective

## Sprint 1 — Foundation and Exploration

### What Went Well

The project established the problem definition, dataset workflow, preprocessing approach, and initial evaluation strategy.

### What Could Be Improved

The project structure and deployment requirements could have been considered earlier.

### Lesson

A clear project structure at the beginning makes later experimentation and deployment easier.

---

## Sprint 2 — Model Development

### What Went Well

The project progressed from baseline experimentation to CNN model development and improvement.

### What Could Be Improved

Model experiments could be tracked more systematically from the beginning.

### Lesson

Recording model configurations and results consistently makes comparison and reproducibility easier.

---

## Sprint 3 — Evaluation and Explainability

### What Went Well

The project expanded evaluation beyond accuracy and included precision, recall, F1-score, ROC-AUC, PR-AUC, confusion-matrix analysis, threshold tuning, and SHAP explainability.

### What Could Be Improved

More extensive external validation and a wider range of test conditions could strengthen future evaluation.

### Lesson

A model should be analyzed from multiple perspectives before deployment.

---

## Sprint 4 — Deployment

### What Went Well

The trained CNN was transformed into a Streamlit application and prepared for public deployment.

The deployment contract was explicitly defined, including:

* RGB input
* 128 × 128 image size
* OpenCV preprocessing
* normalization
* model artifact
* metadata
* selected threshold

Deployment-safe relative paths were introduced, dependencies were pinned, and the public application was tested.

### What Could Be Improved

Deployment testing could include more systematic edge cases and deployment requirements could be planned earlier.

### Lesson

A successful machine learning project requires both model quality and reliable software packaging.

---

# Overall Project Retrospective

## What Went Well

The project successfully progressed through the complete machine learning lifecycle and ended with a public application.

The final project combines:

* Model development
* Evaluation
* Error analysis
* Explainability
* Threshold analysis
* Deployment
* Documentation

## What Could Be Improved

Future projects should establish repository structure, dependency management, experiment tracking, and deployment requirements earlier.

More diverse datasets and external validation should also be considered.

## What I Will Carry Forward

The main lessons from the project are:

1. Machine learning projects require more than a trained model.
2. Reproducibility is essential.
3. Preprocessing must remain consistent between training and deployment.
4. Multiple evaluation metrics provide more information than accuracy alone.
5. False positives and false negatives should be analyzed.
6. Threshold selection affects classification behavior.
7. Explainability helps communicate model behavior.
8. Repository quality and documentation are part of the engineering deliverable.
9. Deployment should be tested from the perspective of a real user.
10. Professional projects should clearly communicate their limitations.
