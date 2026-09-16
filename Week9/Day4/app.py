from pathlib import Path
import json
import io

import numpy as np
import streamlit as st
from PIL import Image
import tensorflow as tf

# ---------- Page setup ----------
st.set_page_config(
    page_title="Lesion Insight | Melanoma Classifier",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Styling ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
    .stApp { background: #f7f8fc; color: #172033; }
    .block-container { max-width: 1180px; padding-top: 2.2rem; padding-bottom: 3rem; }
    h1, h2, h3 { font-family: 'Playfair Display', Georgia, serif; color: #172033; }
    p, label, div, span { font-family: 'DM Sans', Arial, sans-serif; }
    .hero { background: linear-gradient(135deg, #18233f 0%, #2a4772 100%); padding: 2.4rem 2.7rem; border-radius: 22px; color: white; margin-bottom: 1.5rem; box-shadow: 0 14px 30px rgba(33, 55, 95, .16); }
    .hero h1 { color: white; font-size: 2.6rem; margin: 0 0 .35rem 0; }
    .hero p { color: #dbe6f8; font-size: 1.05rem; margin: 0; }
    .eyebrow { text-transform: uppercase; letter-spacing: .15em; font-size: .72rem; font-weight: 700; color: #9ec5ff; margin-bottom: .8rem; }
    .result { padding: 1.2rem 1.4rem; border-radius: 16px; border: 1px solid #dce5f1; background: white; box-shadow: 0 8px 20px rgba(30, 50, 80, .06); }
    .result-good { border-left: 6px solid #2c9b72; }
    .result-alert { border-left: 6px solid #d65a5a; }
    .result-label { color: #68758b; font-size: .8rem; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
    .result-value { font-size: 2.1rem; font-weight: 700; margin-top: .25rem; }
    .muted { color: #68758b; font-size: .92rem; }
    .disclaimer { background: #fff8e8; border: 1px solid #f0d99a; color: #614d1a; padding: .9rem 1rem; border-radius: 12px; font-size: .88rem; }
    [data-testid="stFileUploader"] { background: white; border-radius: 14px; padding: .4rem; }
    .small-note { color: #77839a; font-size: .8rem; }
</style>
""", unsafe_allow_html=True)

# ---------- Model and preprocessing ----------
ARTIFACT_DIR = (
    Path(__file__).resolve().parent / "deployment_artifacts"
)
MODEL_PATH = ARTIFACT_DIR / 'melanoma_cnn.keras'
METADATA_PATH = ARTIFACT_DIR / 'model_metadata.json'

@st.cache_resource
def load_assets():
    metadata = json.loads(METADATA_PATH.read_text(encoding='utf-8'))
    model = tf.keras.models.load_model(MODEL_PATH)
    image_size = (
        int(metadata["input"]["width"]),
        int(metadata["input"]["height"])
    )
    threshold = float(metadata['decision_rule']['selected_threshold'])
    labels = {int(v): k for k, v in metadata['classes'].items()}
    return model, metadata, image_size, threshold, labels

def preprocess_image(image_bytes, image_size):
    """
    Decode and preprocess an uploaded image using Pillow.

    Contract:
    - RGB color format
    - Resize to (width, height)
    - float32 values
    - normalize pixels by 255.0
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        image = image.convert("RGB")
        image = image.resize(image_size, Image.Resampling.LANCZOS)

        image_array = np.asarray(
            image,
            dtype=np.float32
        ) / 255.0

        return np.expand_dims(image_array, axis=0)

    except Exception as exc:
        raise ValueError(
            "The uploaded file is not a readable image."
        ) from exc


# ---------- Header ----------
st.markdown("""<div class="hero"><div class="eyebrow">Interactive model demo · Week 9 Day 3</div><h1>Lesion Insight</h1><p>A focused, human-friendly interface for exploring the melanoma classification model.</p></div>""", unsafe_allow_html=True)

if not MODEL_PATH.exists() or not METADATA_PATH.exists():
    st.error('Deployment artifacts are missing. Please place melanoma_cnn.keras and model_metadata.json in /content/deployment_artifacts.')
    st.stop()

try:
    model, metadata, image_size, default_threshold, labels = load_assets()
except Exception as exc:
    st.error(f'Could not load the model: {exc}')
    st.stop()

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('## About this demo')
    st.write('Upload a clear skin-lesion image to receive the CNN prediction and its malignant probability.')
    threshold = st.slider('Decision threshold', 0.00, 1.00, float(default_threshold), 0.01, help='A prediction is labelled Malignant when the malignant probability is at least this value.')
    st.divider()
    st.markdown('### Serving contract')
    st.caption(f'Input size: {image_size[0]} × {image_size[1]} pixels')
    st.caption('Color format: RGB')
    st.caption('Scaling: float32 / 255')
    st.caption(f'Default threshold: {default_threshold:.2f}')

# ---------- Main interaction ----------
left, right = st.columns([1.05, .95], gap='large')
with left:
    st.markdown('### 1 · Choose an image')
    uploaded = st.file_uploader('Upload a lesion image', type=['jpg', 'jpeg', 'png', 'webp'], help='Supported formats: JPG, JPEG, PNG, WEBP')
    if uploaded is None:
        st.info('Upload an image to activate the prediction panel.')
    else:
        preview = Image.open(io.BytesIO(uploaded.getvalue()))
        st.image(preview, caption=f'Uploaded image · {uploaded.name}', width='stretch')

with right:
    st.markdown('### 2 · Review the result')
    predict_clicked = st.button('Run prediction', type='primary', width='stretch')
    if predict_clicked and uploaded is not None:
        with st.spinner('Analyzing the image…'):
            try:
                x = preprocess_image(uploaded.getvalue(), image_size)
                probability = float(np.asarray(model.predict(x, verbose=0)).squeeze())
                predicted_label = int(probability >= threshold)
                predicted_class = labels[predicted_label]
            except Exception as exc:
                st.error(f'Prediction failed: {exc}')
                st.stop()

        is_malignant = predicted_label == 1
        card_class = 'result-alert' if is_malignant else 'result-good'
        st.markdown(f"""<div class="result {card_class}"><div class="result-label">Model prediction</div><div class="result-value">{predicted_class}</div><div class="muted">Decision threshold: {threshold:.2f}</div></div>""", unsafe_allow_html=True)
        st.write('')
        st.metric('Malignant probability', f'{probability:.1%}')
        st.progress(min(max(probability, 0.0), 1.0), text=f'Malignant probability · {probability:.1%}')

        chart_data = {'Benign': max(0.0, 1.0 - probability), 'Malignant': probability}
        st.bar_chart(chart_data, horizontal=True, height=150, color='#5379ad')
        st.caption('The chart shows the model score before applying the selected threshold.')
    elif uploaded is not None:
        st.info('Ready when you are. Click **Run prediction** to continue.')

st.markdown('')
st.markdown('<div class="disclaimer"><strong>Educational demonstration:</strong> this classifier is not a medical diagnosis and should not replace evaluation by a qualified healthcare professional.</div>', unsafe_allow_html=True)
