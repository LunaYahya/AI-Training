# Melanoma Classifier — Public Demo

Streamlit deployment for Week 9 Day 4.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Model contract
Input: RGB image resized to 128 x 128 and scaled by 255.
Default decision threshold: 0.35 (loaded from model_metadata.json).

## Public URL
Replace this line with the live Space URL after deployment: `PUBLIC_URL = TODO`

Educational demonstration only; not medical advice or diagnosis.
