# Exoplanets Interactive Dashboard

Dashboard interactif réalisé avec **Streamlit** à partir d'un jeu de données sur les exoplanètes.

Le projet fait suite à une analyse exploratoire des données (AED) et propose une interface permettant d'explorer les découvertes d'exoplanètes selon différentes périodes et méthodes de détection.

---

## Dashboard

Le dashboard permet d'explorer les données grâce à deux filtres interactifs :

- période de découverte ;
- une ou plusieurs méthodes de détection.

Les indicateurs et graphiques sont automatiquement actualisés selon la sélection de l'utilisateur.

Le dashboard contient trois vues :

**Population observée** — répartition des exoplanètes par type planétaire.

**Méthodes de détection** — évolution cumulée des découvertes selon les principales méthodes.

**Évolution dans le temps** — nombre de découvertes par année et mise en évidence du pic de découvertes.

---

## Contenu du repository

```text
Dashboard/
│
├── app.py
│   └── Application Streamlit
│
├── projet_E_dataset_exoplanets.csv
│   └── Dataset utilisé par l'application
│
├── cadrage.md
│   └── Message, audience, KPIs et choix de visualisation
│
├── requirements.txt
│   └── Dépendances Python
│
└── README.md
    └── Documentation du projet
```

---

## Stack

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib

---

## Installation

Cloner le repository :

```bash
git clone https://github.com/Nessrine465/Dashboard.git
```

Se placer dans le projet :

```bash
cd Dashboard
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer l'application :

```bash
streamlit run app.py
```

---

## Requirements

```text
streamlit
pandas
numpy
matplotlib
```

---

## Documentation

Les choix de conception du dashboard, le message principal, l'audience cible, les KPIs et la justification des visualisations sont détaillés dans :

 `cadrage.md`

---
