# lung_doctor_pro.py
import streamlit as st

st.set_page_config(page_title="🫁 Lung Doctor Pro", layout="centered")
st.title("🩺 Lung Health Risk Predictor")
st.subheader("Answer these questions to assess your lung condition holistically")

# --- Basic Lifestyle ---
st.markdown("### 🌱 Lifestyle Factors")
water = st.slider("How many glasses of water do you drink daily?", 0, 20, 6)
diet = st.selectbox("How healthy is your daily diet?", ["Poor", "Average", "Healthy"])
exercise = st.selectbox("How often do you exercise in a week?", ["Never", "1-2 times", "3-5 times", "Daily"])
sleep = st.slider("Average sleep hours per night", 0, 12, 6)
stress = st.selectbox("Your current stress level", ["Low", "Moderate", "High"])

# --- Exposure & Habits ---
st.markdown("### 🏭 Environmental & Habits")
smoker = st.selectbox("Do you smoke?", ["No", "Occasionally", "Yes"])
exposure = st.selectbox("Exposed to pollution, dust, or chemicals frequently?", ["No", "Yes"])
age = st.slider("Your Age", 1, 100, 25)

# --- Symptoms ---
st.markdown("### 🤒 Current Symptoms")
symptoms = {
    "Cough": st.checkbox("Cough"),
    "Chest pain": st.checkbox("Chest pain"),
    "Shortness of breath": st.checkbox("Shortness of breath"),
    "Fever": st.checkbox("Fever"),
    "Wheezing": st.checkbox("Wheezing"),
    "Fatigue": st.checkbox("Fatigue"),
    "Coughing up blood": st.checkbox("Coughing up blood"),
    "Weight loss": st.checkbox("Unexplained weight loss")
}

# --- Predict Button ---
if st.button("🧠 Predict Lung Health"):
    score = 0

    # Lifestyle scoring
    if water < 4:
        score += 1
    if diet == "Poor":
        score += 1
    if exercise == "Never":
        score += 1
    if sleep < 5:
        score += 1
    if stress == "High":
        score += 1

    # Environmental and habits
    if smoker == "Yes":
        score += 2
    elif smoker == "Occasionally":
        score += 1
    if exposure == "Yes":
        score += 1
    if age > 50:
        score += 1

    # Symptom scoring
    risky_symptoms = ["Cough", "Coughing up blood", "Shortness of breath", "Weight loss", "Chest pain"]
    for s in risky_symptoms:
        if symptoms[s]:
            score += 2
    for s in symptoms:
        if symptoms[s]:
            score += 1

    # Analysis
    st.subheader("✅ Results")
    if score >= 12:
        st.error("🔴 High Risk of Lung Disease")
        st.markdown("""
        **🛡️ Recommendations:**
        - Visit a pulmonologist immediately  
        - Consider a chest X-ray or CT scan  
        - Stop smoking & avoid pollution  
        - Drink more water & eat fresh foods  
        - Improve sleep and reduce stress
        """)
    elif score >= 7:
        st.warning("🟠 Moderate Risk")
        st.markdown("""
        **🛡️ Recommendations:**
        - Improve your sleep and water intake  
        - Avoid dust, smoke, and stress  
        - Mild symptoms? Monitor carefully  
        """)
    else:
        st.success("🟢 Low Risk – You’re doing good!")
        st.markdown("""
        **Tips:** Keep up your routine. Stay active, hydrated, and avoid pollutants.
        """)

    st.caption("⚠️ This tool is for educational use only. Consult a doctor for medical concerns.")
