import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. CONFIGURATION DE LA PAGE
# ============================================================

st.set_page_config(
    page_title="Exoplanètes — Dashboard",
    layout="wide"
)


# ============================================================
# 2. STYLE DU DASHBOARD
# ============================================================

st.markdown("""
<style>

/* PAGE */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}


/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #F5F7FA;
    border-right: 1px solid #E5E7EB;
}


/* TITRES */
h1 {
    color: #111827 !important;
    font-weight: 750 !important;
    letter-spacing: -0.6px;
}

h2, h3 {
    color: #111827 !important;
    font-weight: 700 !important;
}


/* DESCRIPTION PRINCIPALE */
.dashboard-description {
    color: #6B7280;
    font-size: 16px;
    line-height: 1.6;
    margin-top: -5px;
    margin-bottom: 25px;
}


/* MESSAGE À RETENIR */
.message-box {
    background-color: #F0FDF4;
    border-left: 4px solid #22C55E;
    border-radius: 8px;
    padding: 14px 18px;
    color: #374151;
    font-size: 15px;
    margin-bottom: 30px;
}


/* DESCRIPTION DES GRAPHIQUES */
.graph-description {
    color: #6B7280;
    font-size: 15px;
    line-height: 1.55;
    margin-top: -8px;
    margin-bottom: 20px;
}


/* ONGLETS */
.stTabs [data-baseweb="tab-list"] {
    gap: 32px;
    border-bottom: 1px solid #E5E7EB;
}

.stTabs [data-baseweb="tab"] {
    height: 55px;
    background-color: transparent;
    border-radius: 0;
    padding-left: 3px;
    padding-right: 3px;
    color: #6B7280;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    color: #2563EB !important;
    border-bottom: 3px solid #2563EB !important;
}


/* KPI NATIFS STREAMLIT */
[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E5E7EB;
    padding: 20px 22px;
    border-radius: 14px;
    min-height: 120px;
    box-shadow:
        0 2px 4px rgba(0,0,0,0.03),
        0 8px 20px rgba(0,0,0,0.04);
}

[data-testid="stMetricLabel"] {
    color: #4B5563;
}

[data-testid="stMetricValue"] {
    color: #2563EB;
}


/* SÉPARATEUR */
.separator {
    height: 1px;
    background-color: #E5E7EB;
    margin-top: 35px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 3. CHARGEMENT DES DONNÉES
# ============================================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "projet_E_dataset_exoplanets.csv",
        comment="#"
    )

    # Même filtre que dans le projet AED
    df = df[
        df["default_flag"] == 1
    ].copy()


    # --------------------------------------------------------
    # Classification des planètes utilisée dans l'AED
    # --------------------------------------------------------

    bins = [
        0,
        1.5,
        4,
        10,
        np.inf
    ]

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
# 4. SIDEBAR — FILTRES
# ============================================================

st.sidebar.title("Filtres")

st.sidebar.caption(
    "Explorez les données en faisant varier "
    "la période et les méthodes de détection."
)


# ------------------------------------------------------------
# FILTRE 1 — PÉRIODE
# ------------------------------------------------------------

annee_min = int(
    df["disc_year"].min()
)

annee_max = int(
    df["disc_year"].max()
)


periode = st.sidebar.slider(
    "Période de découverte",
    min_value=annee_min,
    max_value=annee_max,
    value=(annee_min, annee_max)
)


st.sidebar.write("")


# ------------------------------------------------------------
# FILTRE 2 — MÉTHODES
# ------------------------------------------------------------

methodes = sorted(
    df["discoverymethod"]
    .dropna()
    .unique()
    .tolist()
)


methodes_selectionnees = st.sidebar.multiselect(
    "Méthodes de détection",
    options=methodes,
    default=methodes,
    placeholder="Choisissez une ou plusieurs méthodes"
)


st.sidebar.caption(
    "Vous pouvez sélectionner une, plusieurs "
    "ou toutes les méthodes."
)


# ============================================================
# 5. APPLICATION DES FILTRES
# ============================================================

filtered_df = df[
    (df["disc_year"] >= periode[0])
    &
    (df["disc_year"] <= periode[1])
].copy()


if methodes_selectionnees:

    filtered_df = filtered_df[
        filtered_df["discoverymethod"]
        .isin(methodes_selectionnees)
    ].copy()

else:

    st.warning(
        "Sélectionnez au moins une méthode de détection."
    )

    st.stop()


if filtered_df.empty:

    st.warning(
        "Aucune exoplanète ne correspond "
        "aux filtres sélectionnés."
    )

    st.stop()


# ============================================================
# 6. CALCUL DES KPI
# ============================================================


# ------------------------------------------------------------
# KPI 1 — NOMBRE D'EXOPLANÈTES
# ------------------------------------------------------------

nb_planetes = filtered_df[
    "pl_name"
].nunique()


nb_total = df[
    "pl_name"
].nunique()


part_catalogue = (
    nb_planetes
    / nb_total
    * 100
)


# ------------------------------------------------------------
# KPI 2 — MÉTHODE DOMINANTE
# ------------------------------------------------------------

method_counts = (
    filtered_df[
        "discoverymethod"
    ]
    .value_counts()
)


methode_dominante = (
    method_counts.index[0]
)


part_methode = (
    method_counts.iloc[0]
    / method_counts.sum()
    * 100
)


# ------------------------------------------------------------
# KPI 3 — TYPE PLANÉTAIRE DOMINANT
# ------------------------------------------------------------

type_counts_kpi = (
    filtered_df[
        "pl_type"
    ]
    .value_counts()
)


type_dominant = (
    type_counts_kpi.index[0]
)


part_type = (
    type_counts_kpi.iloc[0]
    / type_counts_kpi.sum()
    * 100
)


# ============================================================
# 7. TITRE PRINCIPAL
# ============================================================

st.title(
    "Les méthodes de détection façonnent "
    "notre vision des exoplanètes"
)


st.markdown(
    """
<div class="dashboard-description">
La population d'exoplanètes que nous observons dépend en partie
des techniques utilisées pour les détecter. Explorez les données
pour observer comment les populations et les découvertes évoluent
selon les méthodes et les périodes sélectionnées.
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# 8. MESSAGE PRINCIPAL
# ============================================================

st.markdown(
    """
<div class="message-box">
<b>À retenir :</b> les différentes méthodes de détection ne révèlent
pas les mêmes populations d'exoplanètes. Leur évolution influence
donc directement notre vision de la population planétaire connue.
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# 9. KPI — VUE D'ENSEMBLE
# ============================================================

st.subheader(
    "Vue d'ensemble"
)


col1, col2, col3 = st.columns(
    3,
    gap="medium"
)


# ------------------------------------------------------------
# KPI 1
# ------------------------------------------------------------

with col1:

    st.metric(
        label="Exoplanètes observées",
        value=f"{nb_planetes:,}"
    )

    st.caption(
        f"{part_catalogue:.1f} % du catalogue étudié"
    )


# ------------------------------------------------------------
# KPI 2
# ------------------------------------------------------------

with col2:

    st.metric(
        label="Méthode dominante",
        value=methode_dominante
    )

    st.caption(
        f"{part_methode:.1f} % des découvertes sélectionnées"
    )


# ------------------------------------------------------------
# KPI 3
# ------------------------------------------------------------

with col3:

    st.metric(
        label="Type planétaire dominant",
        value=type_dominant
    )

    st.caption(
        f"{part_type:.1f} % des planètes classifiées"
    )


st.caption(
    f"Analyse basée sur {len(filtered_df):,} observations "
    f"entre {periode[0]} et {periode[1]}."
)


st.markdown(
    '<div class="separator"></div>',
    unsafe_allow_html=True
)


# ============================================================
# 10. ONGLETS — STORYTELLING
# ============================================================

tab1, tab2, tab3 = st.tabs(
    [
        "1 · Population observée",
        "2 · Méthodes de détection",
        "3 · Évolution dans le temps"
    ]
)


# ============================================================
# 11. ONGLET 1 — POPULATION OBSERVÉE
# ============================================================

with tab1:

    labels = [
        "Rocheuse",
        "Super-Terre/Mini-Neptune",
        "Neptunienne",
        "Géante gazeuse"
    ]


    type_counts = (
        filtered_df[
            "pl_type"
        ]
        .value_counts()
        .reindex(labels)
        .fillna(0)
    )


    dominant_type = (
        type_counts.idxmax()
    )


    dominant_value = int(
        type_counts.max()
    )


    total_classifie = int(
        type_counts.sum()
    )


    if total_classifie > 0:

        dominant_percentage = (
            dominant_value
            / total_classifie
            * 100
        )

    else:

        dominant_percentage = 0


    # --------------------------------------------------------
    # TITRE STORYTELLING
    # --------------------------------------------------------

    st.header(
        "Une catégorie domine nettement "
        "la population d'exoplanètes observée"
    )


    st.markdown(
        f"""
<div class="graph-description">
Dans votre sélection, les <b>{dominant_type}</b>
arrivent en tête avec <b>{dominant_percentage:.1f} %</b>
des exoplanètes classifiées.

Modifiez la période ou les méthodes de détection
pour observer si cette domination se maintient.
</div>
""",
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # COULEURS
    # --------------------------------------------------------

    max_value = (
        type_counts.max()
    )

    min_value = (
        type_counts.min()
    )


    colors = []


    for value in type_counts.values:

        if value == max_value:

            # Maximum = vert
            colors.append(
                "#22C55E"
            )

        elif value == min_value:

            # Minimum = rouge
            colors.append(
                "#EF4444"
            )

        else:

            # Valeurs intermédiaires = gris
            colors.append(
                "#D1D5DB"
            )


    # --------------------------------------------------------
    # GRAPHIQUE
    # --------------------------------------------------------

    fig1, ax1 = plt.subplots(
        figsize=(11, 5),
        dpi=120
    )


    bars = ax1.bar(
        type_counts.index,
        type_counts.values,
        color=colors,
        width=0.62
    )


    ax1.set_ylabel(
        "Nombre d'exoplanètes",
        fontsize=11
    )


    ax1.set_xlabel(
        "Type planétaire",
        fontsize=11
    )


    if type_counts.max() > 0:

        ax1.set_ylim(
            0,
            type_counts.max() * 1.15
        )


    ax1.spines[
        "top"
    ].set_visible(False)


    ax1.spines[
        "right"
    ].set_visible(False)


    ax1.grid(
        axis="y",
        alpha=0.12
    )


    ax1.set_axisbelow(
        True
    )


    # --------------------------------------------------------
    # VALEURS AU-DESSUS DES BARRES
    # --------------------------------------------------------

    for bar, value in zip(
        bars,
        type_counts.values
    ):

        ax1.text(

            bar.get_x()
            + bar.get_width() / 2,

            bar.get_height()
            + type_counts.max() * 0.025,

            f"{int(value)}",

            ha="center",

            va="bottom",

            fontsize=11,

            fontweight="bold"
        )


    plt.xticks(
        rotation=8
    )


    plt.tight_layout()


    st.pyplot(
        fig1,
        use_container_width=True
    )


    # --------------------------------------------------------
    # LÉGENDE DES COULEURS
    # --------------------------------------------------------

    st.markdown(
        """
<div style="
display:flex;
gap:28px;
align-items:center;
font-size:13px;
color:#6B7280;
margin-top:-8px;
margin-bottom:15px;
">

<span>
<span style="
display:inline-block;
width:10px;
height:10px;
background:#22C55E;
border-radius:50%;
margin-right:6px;">
</span>
Plus représentée
</span>

<span>
<span style="
display:inline-block;
width:10px;
height:10px;
background:#EF4444;
border-radius:50%;
margin-right:6px;">
</span>
Moins représentée
</span>

<span>
<span style="
display:inline-block;
width:10px;
height:10px;
background:#D1D5DB;
border-radius:50%;
margin-right:6px;">
</span>
Autres catégories
</span>

</div>
""",
        unsafe_allow_html=True
    )


    st.caption(
        "Classification issue de l'AED : "
        "Rocheuse < 1,5 R⊕ ; "
        "Super-Terre/Mini-Neptune : 1,5–4 R⊕ ; "
        "Neptunienne : 4–10 R⊕ ; "
        "Géante gazeuse > 10 R⊕."
    )


# ============================================================
# 12. ONGLET 2 — MÉTHODES DE DÉTECTION
# ============================================================

with tab2:

    # --------------------------------------------------------
    # On prend les 4 méthodes les plus représentées
    # comme dans l'AED
    # --------------------------------------------------------

    top_meth = (
        filtered_df[
            "discoverymethod"
        ]
        .value_counts()
        .head(4)
        .index
    )


    piv = (
        filtered_df[
            filtered_df[
                "discoverymethod"
            ].isin(top_meth)
        ]

        .groupby(
            [
                "disc_year",
                "discoverymethod"
            ]
        )

        .size()

        .unstack(
            fill_value=0
        )

        .cumsum()
    )


    dominant_method = (
        filtered_df[
            "discoverymethod"
        ]
        .value_counts()
        .index[0]
    )


    # --------------------------------------------------------
    # TITRE STORYTELLING
    # --------------------------------------------------------

    st.header(
        "La population observée dépend fortement "
        "des méthodes utilisées pour la détecter"
    )


    st.markdown(
        f"""
<div class="graph-description">
Dans votre sélection, <b>{dominant_method}</b>
est la méthode la plus représentée avec
<b>{part_methode:.1f} %</b> des découvertes.

Comparez plusieurs méthodes pour observer comment
leur contribution évolue au fil du temps.
</div>
""",
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # GRAPHIQUE
    # --------------------------------------------------------

    fig2, ax2 = plt.subplots(
        figsize=(11, 5),
        dpi=120
    )


    couleurs_methodes = [
        "#2563EB",
        "#22C55E",
        "#F59E0B",
        "#8B5CF6"
    ]


    for i, method in enumerate(
        piv.columns
    ):

        ax2.plot(

            piv.index,

            piv[method],

            linewidth=(
                3
                if method == dominant_method
                else 2
            ),

            alpha=(
                1
                if method == dominant_method
                else 0.75
            ),

            color=couleurs_methodes[
                i % len(couleurs_methodes)
            ],

            label=method
        )


    ax2.set_xlabel(
        "Année de découverte",
        fontsize=11
    )


    ax2.set_ylabel(
        "Nombre cumulé de découvertes",
        fontsize=11
    )


    ax2.set_ylim(
        bottom=0
    )


    ax2.spines[
        "top"
    ].set_visible(False)


    ax2.spines[
        "right"
    ].set_visible(False)


    ax2.grid(
        alpha=0.12
    )


    ax2.legend(
        title="Méthode de détection",
        frameon=False
    )


    plt.tight_layout()


    st.pyplot(
        fig2,
        use_container_width=True
    )


    st.caption(
        "Les quatre méthodes les plus représentées "
        "dans la sélection sont affichées pour faciliter "
        "la comparaison."
    )


# ============================================================
# 13. ONGLET 3 — ÉVOLUTION DANS LE TEMPS
# ============================================================

with tab3:

    discoveries_year = (
        filtered_df

        .groupby(
            "disc_year"
        )

        .size()

        .sort_index()
    )


    peak_year = int(
        discoveries_year.idxmax()
    )


    peak_value = int(
        discoveries_year.max()
    )


    # --------------------------------------------------------
    # TITRE STORYTELLING
    # --------------------------------------------------------

    st.header(
        "L'évolution des méthodes a transformé "
        "le rythme des découvertes"
    )


    st.markdown(
        f"""
<div class="graph-description">
Dans la période sélectionnée,
<b>{peak_year}</b> constitue le pic avec
<b>{peak_value:,} exoplanètes découvertes</b>.

Faites varier les méthodes et la période pour identifier
celles qui contribuent aux principales phases
d'accélération des découvertes.
</div>
""",
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # GRAPHIQUE
    # --------------------------------------------------------

    fig3, ax3 = plt.subplots(
        figsize=(11, 5),
        dpi=120
    )


    # --------------------------------------------------------
    # COURBE PRINCIPALE EN BLEU
    # --------------------------------------------------------

    ax3.plot(

        discoveries_year.index,

        discoveries_year.values,

        linewidth=2.5,

        color="#2563EB"
    )


    # --------------------------------------------------------
    # PIC EN VERT
    # --------------------------------------------------------

    ax3.scatter(

        peak_year,

        peak_value,

        s=110,

        color="#22C55E",

        zorder=5
    )


    # --------------------------------------------------------
    # VALEUR DU PIC
    # --------------------------------------------------------

    ax3.annotate(

        f"{peak_value}",

        xy=(
            peak_year,
            peak_value
        ),

        xytext=(
            0,
            14
        ),

        textcoords="offset points",

        ha="center",

        fontsize=11,

        fontweight="bold",

        color="#16A34A"
    )


    # --------------------------------------------------------
    # AXES
    # --------------------------------------------------------

    ax3.set_xlabel(
        "Année de découverte",
        fontsize=11
    )


    ax3.set_ylabel(
        "Nombre d'exoplanètes découvertes",
        fontsize=11
    )


    ax3.set_ylim(
        bottom=0
    )


    # --------------------------------------------------------
    # STYLE
    # --------------------------------------------------------

    ax3.spines[
        "top"
    ].set_visible(False)


    ax3.spines[
        "right"
    ].set_visible(False)


    ax3.grid(
        alpha=0.12
    )


    plt.tight_layout()


    st.pyplot(
        fig3,
        use_container_width=True
    )


    st.caption(
        "La courbe représente le nombre d'exoplanètes "
        "découvertes chaque année. "
        "Le point vert identifie le pic de la période "
        "actuellement sélectionnée."
    )
