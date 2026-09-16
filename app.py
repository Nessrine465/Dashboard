import streamlit as st
import pandas as pd


# --------------------------------------------------
# 1. CHARGEMENT DES DONNÉES
# --------------------------------------------------

@st.cache_data
def load_data():

    # Lecture du fichier CSV
    df = pd.read_csv(
        "projet_E_dataset_exoplanets.csv",
        comment="#"
    )

    # On conserve uniquement les lignes de référence
    df = df[df["default_flag"] == 1].copy()


    # --------------------------------------------------
    # Création du type de planète
    # --------------------------------------------------

    def planet_type(radius):

        # Si le rayon est manquant
        if pd.isna(radius):
            return None

        # Classification selon le rayon
        elif radius < 1.5:
            return "Rocheuse"

        elif radius < 4:
            return "Super-Terre/Mini-Neptune"

        elif radius < 6:
            return "Neptunienne"

        else:
            return "Géante gazeuse"


    # Application de la classification
    df["pl_type"] = df["pl_rade"].apply(planet_type)

    return df


# --------------------------------------------------
# 2. CONFIGURATION DE LA PAGE
# --------------------------------------------------

st.set_page_config(
    page_title="Exoplanètes & méthodes de détection",
    page_icon="🪐",
    layout="wide"
)


# --------------------------------------------------
# 3. CHARGEMENT DU DATASET
# --------------------------------------------------

df = load_data()


# --------------------------------------------------
# 4. TITRE DU DASHBOARD
# --------------------------------------------------

st.title(
    "🪐 Les méthodes de détection façonnent notre vision des exoplanètes"
)

st.write(
    "Explorez comment les différentes méthodes de détection "
    "influencent les caractéristiques des exoplanètes que nous observons."
)


# --------------------------------------------------
# 5. GRAPHIQUE 1
# Répartition par type planétaire
# --------------------------------------------------

st.subheader("Répartition par type planétaire")

# Compter le nombre de planètes dans chaque catégorie
type_counts = df["pl_type"].value_counts()

# Affichage du graphique
st.bar_chart(type_counts)