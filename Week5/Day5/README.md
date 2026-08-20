# Day 5 — Phase 3 Project Selection & Sprint 1 Planning
## 1. Phase 3 Overview
Phase 3 is the applied part of the training program. The goal is to build one complete AI/ML project from data collection and analysis to model development and deployment across four sprints.
The four sprints are:
- **Sprint 1:** Data understanding, EDA, and baseline model.
- **Sprint 2:** Model development and comparison.
- **Sprint 3:** Feature engineering and hyperparameter tuning.
- **Sprint 4:** Deployment, documentation, and finalization.
---
## 2. Selected Project
### Cardiac Patient Monitoring System
- **Dataset:** Heart Disease Health Indicators Dataset
- **Problem Type:** Binary Classification
- **Target:** `HeartDiseaseorAttack`
- **Classes:** `0` and `1`
The project was selected because it was already explored during the previous phase. The existing work will be improved, reorganized, and extended into a complete end-to-end project.
---
## 3. Problem Statement
Heart disease is an important health concern, and health-related data can contain patterns associated with heart disease or heart attack indicators.
This project aims to analyze health, lifestyle, and demographic factors and develop a binary classification model to predict the `HeartDiseaseorAttack` target.
The system is intended for machine learning prediction and analysis, not for medical diagnosis.
---
## 4. Definition of Done
The project will be considered complete when it includes:
- [x] Data cleaning and preprocessing
- [x] Exploratory Data Analysis
- [x] Baseline model
- [x] Multiple model evaluation
- [x] Classification metrics and confusion matrix
- [x] Feature engineering and tuning
- [x] Final model selection
- [ ] Saved model artifact
- [ ] Public deployment
- [ ] Complete README and documentation
- [x] `requirements.txt`
- [ ] Final technical write-up
- [ ] Complete GitHub branch/PR workflow
The checked items were already completed during previous work, while the remaining items will be completed during Phase 3.
---
## 5. Sprint 1 Goal
 **Understand the dataset, complete the initial EDA, and establish a reproducible baseline classification model.**
### Sprint 1 Backlog
| Task | Estimated Effort |
|---|---:|
| Dataset documentation | 1 hour |
| Data cleaning | 1.5 hours |
| EDA | 3 hours |
| Baseline model | 2 hours |
| Model evaluation | 1 hour |
| Documentation | 1.5 hours |
**Total estimated effort: 10 hours**
---
## 6. Acceptance Criteria
Each task is considered complete when:
- The code runs without errors.
- Results are documented in Markdown.
- The task produces the expected output.
- Changes are committed with a clear message.
- Work is pushed to the correct feature branch.
- A Pull Request is created for mentor review.
- Model metrics are recorded and compared with the baseline.
---
## 7. GitHub Workflow
The project will use a feature-branch workflow:
```text
main
 ↓
Feature Branch
 ↓
Development
 ↓
Commit
 ↓
Push
 ↓
Pull Request
 ↓
Mentor Review
 ↓
Merge