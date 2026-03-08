from ai_diagnosis import get_ai_diagnosis
import streamlit as st
import numpy as np
from PIL import Image

from preprocess_image import preprocess_image
from severity import grade_severity
from recommendation import get_recommendations

st.title("Leaf Health Check")

st.write("Upload a plant leaf image to analyze plant health.")

uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg","png","jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf", use_container_width=True)

    img = np.array(image)

    # Analysis loading spinner
    with st.spinner("Analyzing leaf health..."):
        percent = preprocess_image(img)

    severity, disease = grade_severity(percent)

    st.subheader("Diagnosis Result")

    st.write("Affected Area:", round(percent,2),"%")

    # Progress bar
    st.progress(int(percent))

    # Colored severity display
    if severity == "Healthy":
        st.success(f"Severity Level: {severity}")
    elif severity == "Mild":
        st.info(f"Severity Level: {severity}")
    elif severity == "Moderate":
        st.warning(f"Severity Level: {severity}")
    else:
        st.error(f"Severity Level: {severity}")

    st.write("Possible Disease:", disease)

    # AI Diagnosis (safe fallback if API fails)
    ai_result = get_ai_diagnosis(severity)

    st.subheader("AI Diagnosis")
    st.write(ai_result)

    st.subheader("Rescue Tips")

    tips = get_recommendations()

    for tip in tips:
        st.write("-", tip)

    report = f"""
Leaf Health Check Report

Affected Area: {round(percent,2)} %
Severity Level: {severity}
Possible Disease: {disease}

AI Diagnosis:
{ai_result}

Rescue Tips:
1. Maintain proper watering schedule
2. Ensure adequate sunlight
3. Remove infected leaves
4. Use appropriate fertilizer
5. Improve airflow around plant
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="leaf_health_report.txt",
        mime="text/plain"
    )