import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Exoplanètes", page_icon="✦", layout="wide")

st.markdown("""
<style>
:root { --ink:#172033; --muted:#667085; --line:#e7eaf0; --paper:#fbfcfe; --accent:#6874c9; }
.stApp { background:var(--paper); }
[data-testid="stHeader"] { background:var(--paper); }
[data-testid="stToolbar"] { visibility:hidden; }
[data-testid="stSidebar"] { background:#f2f4f8; }
[data-testid="stSidebar"] > div:first-child { padding:2rem 1.25rem; }
[data-testid="stSidebar"] label, [data-testid="stSidebar"] p { color:var(--muted) !important; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color:var(--ink) !important; }
.block-container { max-width:1320px; padding:2.5rem 3.25rem 4rem; }
h1, h2, h3 { color:var(--ink) !important; letter-spacing:-.035em; }
h1 { font-size:clamp(2.2rem, 4vw, 3.4rem) !important; line-height:1.05 !important; }
h2 { font-size:1.55rem !important; }
.intro { color:var(--muted); font-size:1rem; line-height:1.55; max-width:720px; margin:.7rem 0 1.7rem; }
.selection { color:var(--muted); font-size:.86rem; margin:.8rem 0 1.4rem; }
[data-testid="stMetric"] { background:#fff; border:1px solid var(--line); border-radius:14px; padding:1rem 1.15rem; min-height:108px; box-shadow:0 6px 18px rgba(23,32,51,.035); }
[data-testid="stMetricLabel"] { color:var(--muted); font-size:.8rem; font-weight:700; }
[data-testid="stMetricValue"] { color:var(--accent); font-size:1.45rem; }
[data-baseweb="select"] > div { background:#fff !important; border-color:#d9deea !important; }
[data-baseweb="select"] input { color:var(--ink) !important; }
[data-baseweb="select"] [data-testid="stMarkdownContainer"],
[data-baseweb="select"] [data-testid="stMarkdownContainer"] p { color:var(--ink) !important; }
[data-baseweb="tag"] { background:#e9ecfa !important; color:#4f5eae !important; }
[data-baseweb="tag"] span { color:#4f5eae !important; }
[role="listbox"] { background:#fff !important; }
[role="option"], [role="option"] * { color:var(--ink) !important; background:#fff !important; }
.stTabs [data-baseweb="tab-list"] { gap:1.4rem; border-bottom:1px solid var(--line); }
.stTabs [data-baseweb="tab"] { height:46px; color:var(--muted); font-weight:700; font-size:.9rem; }
.stTabs [aria-selected="true"] { color:var(--accent) !important; border-bottom:2px solid var(--accent) !important; }
@media (max-width:800px) { .block-container { padding:1.5rem 1rem 3rem; } }
</style>
""", unsafe_allow_html=True)

plt.rcParams.update({
    "figure.facecolor":"#ffffff", "axes.facecolor":"#ffffff", "axes.edgecolor":"#dfe3ec",
    "axes.labelcolor":"#667085", "xtick.color":"#667085", "ytick.color":"#667085",
    "text.color":"#344054", "font.size":10,
})


@st.cache_data
def load_data():
    data = pd.read_csv("projet_E_dataset_exoplanets.csv", comment="#")
    data = data[data["default_flag"] == 1].copy()
    data["pl_type"] = pd.cut(
        data["pl_rade"], [0, 1.5, 4, 10, np.inf],
        labels=["Rocheuse", "Super-Terre / Mini-Neptune", "Neptunienne", "Géante gazeuse"],
    )
    return data


df = load_data()
year_min, year_max = int(df["disc_year"].min()), int(df["disc_year"].max())
method_counts = df["discoverymethod"].value_counts()
methods = method_counts.index.tolist()
main_methods = methods[:4]

METHOD_COLORS = {
    "Transit": "#6874c9",
    "Radial Velocity": "#6ca89b",
    "Microlensing": "#b39ac7",
    "Imaging": "#d19a62",
}
TYPE_ACCENT = "#6874c9"
TYPE_NEUTRAL = "#dfe3ee"

# Repères externes : grandes missions spatiales qui ont changé la recherche
# d'exoplanètes. Le CSV ne contient pas de colonne "telescope", donc ces
# repères sont affichés comme contexte, jamais comme attribution individuelle.
SURVEY_MILESTONES = {
    2006: ("CoRoT", "#b39ac7"),
    2009: ("Kepler", "#6874c9"),
    2014: ("K2", "#93a1d8"),
    2018: ("TESS", "#6ca89b"),
}

st.sidebar.title("Filtres")
st.sidebar.caption("Choisissez une période et une ou plusieurs méthodes.")
st.session_state.setdefault("period_filter", (year_min, year_max))
st.session_state.setdefault("method_filter", main_methods)

period = st.sidebar.slider("Période de découverte", year_min, year_max, key="period_filter")
selected_methods = st.sidebar.multiselect(
    "Méthodes de détection", methods, key="method_filter", placeholder="Sélectionner des méthodes"
)
st.sidebar.caption(f"{len(selected_methods)} méthode(s) sélectionnée(s) sur {len(methods)}.")

if not selected_methods:
    st.info("Sélectionnez au moins une méthode pour afficher les résultats.")
    st.stop()

filtered = df[
    df["disc_year"].between(period[0], period[1]) & df["discoverymethod"].isin(selected_methods)
].copy()
if filtered.empty:
    st.info("Aucune découverte ne correspond à cette sélection.")
    st.stop()

planet_count = filtered["pl_name"].nunique()
method_summary = filtered["discoverymethod"].value_counts()
dominant_method = method_summary.index[0]
method_share = method_summary.iloc[0] / len(filtered) * 100
top_method_count = min(4, len(method_summary))
type_summary = filtered["pl_type"].value_counts().dropna()
dominant_type = type_summary.index[0] if not type_summary.empty else "Non classifié"
type_share = type_summary.iloc[0] / type_summary.sum() * 100 if not type_summary.empty else 0

st.title("Notre carte des exoplanètes dépend de la façon dont nous les cherchons")
st.caption(f"{period[0]}–{period[1]} · {len(selected_methods)} méthodes · {len(filtered):,} observations")

kpi_1, kpi_2, kpi_3 = st.columns(3, gap="medium")
with kpi_1:
    st.metric("Planètes dans la sélection", f"{planet_count:,}")
with kpi_2:
    st.metric("Méthode la plus utilisée", dominant_method)
    st.caption(f"{method_summary.iloc[0]:,} · {method_share:.1f} %")
with kpi_3:
    st.metric("Type le plus représenté", dominant_type)
    st.caption(f"{type_summary.iloc[0]:,} · {type_share:.1f} %" if not type_summary.empty else "Non classifié")

st.caption(f"À retenir : {dominant_method} représente {method_share:.1f} % des découvertes de cette sélection.")

st.divider()

labels = ["Rocheuse", "Super-Terre / Mini-Neptune", "Neptunienne", "Géante gazeuse"]
counts = filtered["pl_type"].value_counts().reindex(labels).fillna(0)
annual = filtered.groupby("disc_year").size().sort_index()
peak_year, peak_count = int(annual.idxmax()), int(annual.max())

tab_population, tab_methods, tab_time = st.tabs(
    ["Population observée", "Méthodes de détection", "Évolution dans le temps"]
)

with tab_population:
    st.markdown(
        f"<h2>Les <span style='color:{TYPE_ACCENT}'>{dominant_type}</span> "
        "ne sont pas représentées à parts égales</h2>",
        unsafe_allow_html=True,
    )
    fig, ax = plt.subplots(figsize=(7, 4.6), dpi=120)
    colors = [TYPE_ACCENT if value == counts.max() else TYPE_NEUTRAL for value in counts]
    bars = ax.barh(counts.index, counts.values, color=colors, edgecolor="none")
    ax.invert_yaxis(); ax.set_xlabel("Planètes"); ax.grid(axis="x", alpha=.15)
    ax.set_axisbelow(True); ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    for bar, value in zip(bars, counts.values):
        ax.text(bar.get_width() + counts.max() * .02, bar.get_y() + bar.get_height() / 2, f"{int(value):,}", va="center", fontweight="bold")
    ax.set_xlim(0, max(counts.max() * 1.18, 1)); fig.tight_layout(); st.pyplot(fig, width="stretch")
    st.caption(f"{dominant_type} : {type_share:.1f} % des planètes classifiées.")

with tab_methods:
    method_accent = METHOD_COLORS.get(dominant_method, TYPE_ACCENT)
    st.markdown(
        f"<h2>Le <span style='color:{method_accent}'>{dominant_method}</span> "
        f"domine les {top_method_count} méthodes principales</h2>",
        unsafe_allow_html=True,
    )
    top_methods = method_summary.head(4).sort_values()
    fig, ax = plt.subplots(figsize=(11, 4.8), dpi=120)
    colors = [METHOD_COLORS.get(method, "#dfe3ee") for method in top_methods.index]
    bars = ax.barh(top_methods.index, top_methods.values, color=colors, edgecolor="none")
    ax.set_xlabel("Découvertes"); ax.grid(axis="x", alpha=.15); ax.set_axisbelow(True)
    ax.spines[["top", "right", "left"]].set_visible(False); ax.tick_params(axis="y", length=0)
    for bar, value in zip(bars, top_methods.values):
        ax.text(bar.get_width() + top_methods.max() * .02, bar.get_y() + bar.get_height() / 2, f"{int(value):,}", va="center", fontweight="bold")
    ax.set_xlim(0, max(top_methods.max() * 1.2, 1)); fig.tight_layout(); st.pyplot(fig, width="stretch")
    st.caption(f"Ces 4 méthodes représentent {top_methods.sum() / method_summary.sum() * 100:.1f} % des découvertes sélectionnées.")

    cumulative = (
        filtered[filtered["discoverymethod"].isin(top_methods.index)]
        .groupby(["disc_year", "discoverymethod"]).size().unstack(fill_value=0).sort_index().cumsum()
    )
    fig, ax = plt.subplots(figsize=(11, 4.5), dpi=120)
    for index, method in enumerate(cumulative.columns):
        ax.plot(
            cumulative.index,
            cumulative[method],
            label=method,
            color=METHOD_COLORS.get(method, "#c7cddd"),
            linewidth=2.8 if method == dominant_method else 2.0,
        )
    ax.set_xlabel("Année"); ax.set_ylabel("Découvertes cumulées"); ax.grid(alpha=.15); ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False); ax.legend(frameon=False, ncol=2)
    fig.tight_layout(); st.pyplot(fig, width="stretch")

with tab_time:
    st.markdown(
        f"<h2>Les nouvelles missions coïncident avec une forte accélération du "
        f"<span style='color:{METHOD_COLORS.get(dominant_method, TYPE_ACCENT)}'>{dominant_method}</span></h2>",
        unsafe_allow_html=True,
    )
    peak_year, peak_count = int(annual.idxmax()), int(annual.max())
    fig, ax = plt.subplots(figsize=(11, 5), dpi=120)
    transit_color = METHOD_COLORS.get("Transit", TYPE_ACCENT)
    ax.plot(annual.index, annual.values, color=transit_color, linewidth=2.5)
    ax.fill_between(annual.index, annual.values, color=transit_color, alpha=.10)
    ax.scatter(peak_year, peak_count, color=transit_color, s=70, zorder=3)
    ax.annotate(f"Pic : {peak_year} · {peak_count:,}", (peak_year, peak_count), xytext=(0, 14), textcoords="offset points", ha="center", fontweight="bold")
    if period[0] <= 2002 <= period[1] and "Transit" in selected_methods:
        ax.axvline(2002, color=transit_color, linestyle="--", linewidth=1.5)
        ax.text(2002.3, max(annual.values) * .88, "Transit apparaît", color=transit_color, fontsize=9)
        ax.axvspan(2002, period[1], color=transit_color, alpha=.06)
    for index, (launch_year, (mission, mission_color)) in enumerate(SURVEY_MILESTONES.items()):
        if period[0] <= launch_year <= period[1]:
            ax.axvline(launch_year, color=mission_color, linestyle=":", linewidth=1.5)
            ax.text(
                launch_year + .25,
                max(annual.values) * (.72 - index % 2 * .12),
                f"{mission}\n{launch_year}",
                color=mission_color,
                fontsize=8,
                va="top",
            )
    ax.set_xlabel("Année"); ax.set_ylabel("Découvertes"); ax.grid(alpha=.15); ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False); fig.tight_layout(); st.pyplot(fig, width="stretch")
    st.caption("L'histoire du catalogue est aussi une histoire de capacité de détection.")
