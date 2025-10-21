import streamlit as st

st.set_page_config(page_title="🩺 Lung Doctor Pro max", layout="centered")
st.title("🩺 Lung Doctor Pro")
st.subheader("AI-assisted lung health check-up")

# --- User Inputs ---
st.markdown("### 🌱 Lifestyle & Personal Info")
age = st.slider("Age", 1, 100, 25)
water = st.slider("How many glasses of water do you drink daily?", 0, 20, 6)
diet = st.selectbox("Your regular diet?", ["Poor", "Average", "Healthy"])
exercise = st.selectbox("Exercise routine?", ["Never", "1–2 times/week", "3–5 times/week", "Daily"])
sleep = st.slider("Average sleep per night (hrs)", 0, 12, 6)
stress = st.selectbox("Stress level", ["Low", "Moderate", "High"])
smoker = st.selectbox("Do you smoke?", ["No", "Occasionally", "Yes"])
exposure = st.selectbox("Exposed to dust/pollution/chemicals?", ["No", "Yes"])

st.markdown("### 🤒 Symptoms")
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
    symptom_count = sum(symptoms.values())
    condition = "Unknown"
    onset = "Not enough data"
    prevention_window = "-"
    reversible = "Unknown"
    recovery_days = "-"
    recovery_chance = "-"
    actions = []
    avoid = []

    # Match diseases
    if symptoms["Cough"] and symptoms["Fever"] and symptoms["Shortness of breath"]:
        condition = "Pneumonia"
        score += 4
        onset = "5–7 days ago"
        prevention_window = "3–5 more days"
        reversible = "Yes"
        recovery_days = "10–14 days"
        recovery_chance = "90%"
        actions += ["Doctor visit within 48 hrs", "Start antibiotics if prescribed", "Drink 3+ L water/day", "Take full rest"]
        avoid += ["Cold drinks", "Outdoor smoke", "Delaying treatment"]

    elif symptoms["Cough"] and symptoms["Coughing up blood"] and symptoms["Weight loss"]:
        condition = "Tuberculosis (TB)"
        score += 5
        onset = "2+ weeks ago"
        prevention_window = "Urgent – may become chronic"
        reversible = "Partially (if caught early)"
        recovery_days = "1–2 months (under treatment)"
        recovery_chance = "80% with adherence"
        actions += ["See a chest specialist ASAP", "Get a sputum test and chest X-ray", "Avoid physical exertion"]
        avoid += ["Skipping meds", "Delaying diagnosis", "Public exposure (if untreated)"]

    elif smoker != "No" and symptoms["Cough"] and symptoms["Shortness of breath"]:
        condition = "COPD (Chronic Obstructive Pulmonary Disease)"
        score += 6
        onset = "Likely several months"
        prevention_window = "Very limited"
        reversible = "No – manageable only"
        recovery_days = "Chronic, needs lifetime care"
        recovery_chance = "Manageable with 60–70% efficiency"
        actions += ["Immediate pulmonary test", "Stop smoking now", "Start breathing exercises", "Inhaler if prescribed"]
        avoid += ["Smoking", "Dust exposure", "Cold weather", "Overexertion"]

    elif symptoms["Wheezing"] and symptoms["Shortness of breath"]:
        condition = "Asthma"
        score += 3
        onset = "Few days–weeks"
        prevention_window = "Good if treated early"
        reversible = "Yes (in mild/moderate)"
        recovery_days = "7–10 days"
        recovery_chance = "95% with inhaler & rest"
        actions += ["Avoid dust/pollen", "Use inhaler as prescribed", "Monitor breath regularly"]
        avoid += ["Overexertion", "Smoke", "Skipping meds"]

    elif symptom_count >= 2:
        condition = "Mild lung inflammation / infection"
        onset = "2–4 days ago"
        prevention_window = "Next 5–7 days"
        reversible = "Yes"
        recovery_days = "5–8 days"
        recovery_chance = "98%"
        actions += ["Rest well", "Drink warm fluids", "Avoid stress", "Take paracetamol if feverish"]
        avoid += ["Cold air", "Heavy exercise", "Junk food"]

    else:
        condition = "No major indicators found"
        onset = "N/A"
        prevention_window = "N/A"
        reversible = "-"
        recovery_days = "-"
        recovery_chance = "-"
        actions += ["Maintain hydration", "Avoid stress", "Track any new symptoms"]
        avoid += ["Unhygienic food", "Poor sleep"]

    # Display Results
    st.success("✅ Prediction Complete")

    st.markdown(f"""
### 🔎 Likely Condition: `{condition}`

🧭 **Estimated Symptom Onset:** {onset}  
⏳ **Prevention Window:** {prevention_window}  
🔁 **Reversible?** {reversible}  
📉 **Severity:** `{ "High" if score >= 6 else "Moderate" if score >= 3 else "Low" }`  
📅 **Estimated Recovery Time:** {recovery_days}  
💊 **Recovery Probability:** {recovery_chance}
""")

    st.markdown("### 🛡️ What You MUST Do:")
    for act in actions:
        st.markdown(f"- ✅ {act}")

    st.markdown("### 🚫 What to AVOID:")
    for a in avoid:
        st.markdown(f"- ❌ {a}")

    st.caption("⚠️ This tool does not replace a doctor. Always consult a physician if symptoms worsen or persist.")
