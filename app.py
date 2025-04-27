import streamlit as st

st.title("Simulateur de Couverture Santé")

age = st.number_input("Votre âge :", min_value=0, max_value=120)
code_postal = st.text_input("Votre code postal :")
soins = st.multiselect(
    "Avez-vous des dépenses de santé régulières pour :",
    ["Optique", "Dentaire", "Hospitalisation", "Médecine douce"]
)

if st.button("Vérifier ma couverture"):
    if age > 65 or "Hospitalisation" in soins:
        st.warning("⚠️ Nous recommandons une option complémentaire.")
    else:
        st.success("✅ Votre couverture standard est suffisante.")
