import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Détail des exoplanètes",
    layout="wide"
)

# ============================================================
# CHARGEMENT DES DONNÉES
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv(
        "projet_E_dataset_exoplanets.csv",
        comment="#"
    )

    df = df[df["default_flag"] == 1].copy()

    bins = [0, 1.5, 4, 10, np.inf]

    labels = [
        "Rocheuse",
        "Super-Terre/Mini-Neptune",
        "Neptunienne",
        "Géante gazeuse"
    ]

    df["pl_type"] = pd.cut(
        df["pl_rade"],
        bins=bins,
        labels=labels
    )

    return df


df = load_data()


# ============================================================
# TITRE
# ============================================================

st.title("🔎 Détail des exoplanètes")

st.write(
    """
Cette vue complète le dashboard principal en permettant
d'explorer directement les exoplanètes présentes dans le catalogue.
"""
)


# ============================================================
# FILTRES
# ============================================================

col1, col2 = st.columns(2)

with col1:
    methodes = sorted(
        df["discoverymethod"].dropna().unique()
    )

    methode = st.multiselect(
        "Méthode de détection",
        methodes,
        default=methodes
    )


with col2:
    types = [
        "Rocheuse",
        "Super-Terre/Mini-Neptune",
        "Neptunienne",
        "Géante gazeuse"
    ]

    types_selectionnes = st.multiselect(
        "Type planétaire",
        types,
        default=types
    )


# ============================================================
# APPLICATION DES FILTRES
# ============================================================

detail_df = df[
    df["discoverymethod"].isin(methode)
    &
    df["pl_type"].isin(types_selectionnes)
].copy()


# ============================================================
# NOMBRE DE RÉSULTATS
# ============================================================

st.metric(
    "Exoplanètes correspondant à la sélection",
    detail_df["pl_name"].nunique()
)


# ============================================================
# TABLEAU
# ============================================================

colonnes = [
    "pl_name",
    "hostname",
    "discoverymethod",
    "disc_year",
    "pl_type",
    "pl_rade"
]


table = detail_df[
    colonnes
].copy()


table = table.rename(
    columns={
        "pl_name": "Exoplanète",
        "hostname": "Étoile hôte",
        "discoverymethod": "Méthode",
        "disc_year": "Année",
        "pl_type": "Type planétaire",
        "pl_rade": "Rayon (R⊕)"
    }
)


st.subheader("Catalogue détaillé")

st.dataframe(
    table,
    use_container_width=True,
    hide_index=True
)