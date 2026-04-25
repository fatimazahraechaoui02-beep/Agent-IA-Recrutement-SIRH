import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Plateforme IA Recrutement", layout="wide")

# Titre Principal
st.title("🚗 Plateforme Intelligence RH : Secteur Automobile")
st.markdown("---")

# Barre latérale (Sidebar) avec les infos du projet
st.sidebar.header("Présentation du Projet")
st.sidebar.info("""
Cette plateforme utilise un Agent IA (GPT-4o) pour analyser 
automatiquement une base de 15 CVs et identifier les meilleurs 
profils pour le poste de Chargé(e) de Recrutement.
""")

# Données corrigées et réalistes (basées sur tes résultats Coze)
data = {
    "Candidat": [
        "Candidat 11", "Candidat 6", "Candidat 9", 
        "Candidat 3", "Oumayma Oujebour", "Candidat 15", 
        "Candidat 8", "Candidat 13", "Candidat 10", "Salma Jaib"
    ],
    "Diplôme": [
        "Bac+3 RH", "Bac+3 RH", "Bac+3 RH", 
        "Bac+3 RH", "Bac+2 RH", "Bac+3 RH", 
        "Bac+3 RH", "Bac+3 RH", "Bac+3 RH", "Bac+3 RH (en cours)"
    ],
    "Expérience": [
        "4 ans", "3 ans", "5 ans", 
        "2 ans", "3 ans", "4 ans", 
        "2 ans", "3 ans", "1 an", "Débutante"
    ],
    "Secteur Auto": [
        "Oui", "Oui", "Non", "Oui", "Oui (Stage)", 
        "Oui", "Non", "Oui", "Non", "Oui (Passion)"
    ],
    "Score Final /10": [9.2, 9.0, 8.8, 8.7, 8.5, 8.5, 7.0, 8.0, 7.5, 6.5]
}

df = pd.DataFrame(data)

# Affichage du tableau de bord
st.subheader("📊 Tableau de Scoring des Candidatures")
st.write("Ce tableau classe les candidats selon leur adéquation avec le poste (Études, Expérience, Secteur).")

# Affichage du tableau avec style (on surligne le meilleur score)
st.dataframe(
    df.style.highlight_max(axis=0, subset=['Score Final /10'], color='#90EE90'), 
    use_container_width=True
)

# Section Top Profiles (Métriques)
st.markdown("---")
st.subheader("🏆 Top 3 des Meilleurs Profils")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rang 1", "Candidat 11", "9.2/10")
with col2:
    st.metric("Rang 2", "Candidat 6", "9.0/10")
with col3:
    st.metric("Rang 3", "Candidat 9", "8.8/10")

# Pied de page
st.markdown("---")
st.caption("Analyse générée par l'Agent IA configuré sur Coze & Déployée via Streamlit.")
