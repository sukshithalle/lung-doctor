# lung_doctor.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="🫁 Lung Disease Doctor", layout="centered")
st.title("🩺 Lung Disease Predictor")
st.subheader("Answer a few quick questions to assess your lung health")

symptoms = {
    "Cough": st.checkbox("Cough"),
    "Chest pain": st.checkbox("Chest pain"),
    "Shortness of breath": st.checkbox("Shortness of breath"),
    "Fever": st.checkbox("Fever"),
    "Wheezing": st.checkbox("Wheezing"),
    "Fatigue": st.checkbox("Fatigue"),
    "Coughing up blood": st.checkbox("Coughing up blood"),
    "Weight loss": st.checkbox("Unexplained weight loss"),
}

age = st.slider("Your Age", 1, 100, 25)
smoker = st.selectbox("Do you smoke?", ["No", "Yes"])
exposure = st.selectbox("Exposed to air pollution or chemicals?", ["No", "Yes"])
submit = st.button("🧠 Predict Possible Conditions")


def diagnose(symptoms, age, smoker, exposure):
    conditions = []

    if symptoms["Cough"] and symptoms["Fever"] and symptoms["Shortness of breath"]:
        conditions.append({
            "name": "Pneumonia",
            "desc": "An infection that inflames the air sacs in one or both lungs.",
            "tip": "Drink fluids, rest well, and see a doctor if symptoms worsen."
        })

    if symptoms["Cough"] and symptoms["Coughing up blood"] and age > 40:
        conditions.append({
            "name": "Tuberculosis",
            "desc": "A potentially serious infectious disease that mainly affects the lungs.",
            "tip": "Seek a TB test and chest X-ray immediately."
        })

    if symptoms["Wheezing"] and symptoms["Shortness of breath"] and smoker == "Yes":
        conditions.append({
            "name": "COPD",
            "desc": "Chronic Obstructive Pulmonary Disease, common among smokers.",
            "tip": "Avoid smoking, use prescribed inhalers, consult a pulmonologist."
        })

    if symptoms["Chest pain"] and symptoms["Shortness of breath"]:
        conditions.append({
            "name": "Asthma",
            "desc": "A condition where your airways narrow and swell, producing extra mucus.",
            "tip": "Avoid allergens, use inhalers, consider lung function tests."
        })

    if symptoms["Coughing up blood"] and symptoms["Weight loss"] and age > 45:
        conditions.append({
            "name": "Lung Cancer (early signs)",
            "desc": "Warning signs that require immediate attention and imaging.",
            "tip": "Consult a specialist for CT scan or biopsy screening."
        })

    if not conditions:
        return [{
            "name": "Low Risk",
            "desc": "Your symptoms don’t match major lung diseases.",
            "tip": "Stay hydrated, rest well, and monitor symptoms."
        }]

    return conditions


if submit:
    with st.spinner("Analyzing symptoms..."):
        result = diagnose(symptoms, age, smoker, exposure)
        st.success("✅ Prediction Complete")
        st.subheader("🧾 Possible Conditions:")

        for cond in result:
            st.markdown(f"### 🩺 {cond['name']}")
            st.write(cond["desc"])
            st.info(f"🛡️ Precaution: {cond['tip']}")

        st.caption("⚠️ This tool does not replace a medical professional. Always consult a doctor.")
