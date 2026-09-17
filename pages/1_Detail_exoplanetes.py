import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Détail des exoplanètes",
    page_icon="⌕",
    layout="wide"
)

st.markdown("""
<style>
:root { --ink: #172033; --muted: #667085; --line: #e7eaf0; --paper: #fbfcfe; --blue: #335cff; }
.stApp { background: var(--paper); }
.block-container { padding: 2.75rem 3.5rem 4rem; max-width: 1400px; }
h1, h2, h3 { color: var(--ink) !important; letter-spacing: -0.04em; }
h1 { font-size: clamp(2.1rem, 4vw, 3.3rem) !important; line-height: 1.05 !important; }
.eyebrow { color: var(--blue); font-size: .72rem; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; margin-bottom: .8rem; }
.intro { color: var(--muted); font-size: 1rem; line-height: 1.6; max-width: 700px; margin: 1rem 0 2rem; }
[data-testid="stMetric"] { background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.25rem; box-shadow: 0 8px 24px rgba(23,32,51,.045); }
[data-baseweb="select"] > div { background: #fff !important; border-color: #d9deea !important; }
[data-baseweb="select"] input { color: var(--ink) !important; }
[data-baseweb="select"] [data-testid="stMarkdownContainer"],
[data-baseweb="select"] [data-testid="stMarkdownContainer"] p { color: var(--ink) !important; }
[data-baseweb="tag"] { background: #e9ecfa !important; color: #4f5eae !important; }
[data-baseweb="tag"] span { color: #4f5eae !important; }
[role="listbox"] { background: #fff !important; }
[role="option"], [role="option"] * { color: var(--ink) !important; background: #fff !important; }
div[data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: 12px; overflow: hidden; }
@media (max-width: 800px) { .block-container { padding: 2rem 1.1rem 3rem; } }
</style>
""", unsafe_allow_html=True)

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

st.markdown('<div class="eyebrow">CATALOGUE · EXPLORATION</div>', unsafe_allow_html=True)
st.title("Parcourir le catalogue")

st.write(
    """
Cette vue complète le tableau de bord avec les lignes du catalogue.
Filtrez les méthodes et les types pour retrouver les mondes qui vous intéressent.
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
    width="stretch",
    hide_index=True
)
