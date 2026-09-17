# Exoplanets Interactive Dashboard

Dashboard interactif réalisé avec **Streamlit** à partir d'un jeu de données sur les exoplanètes.

Le projet fait suite à une analyse exploratoire des données (AED) et propose une interface permettant d'explorer les découvertes d'exoplanètes selon différentes périodes et méthodes de détection.

---

## Application déployée

Le dashboard est accessible en ligne sur Streamlit Community Cloud :

👉 **[Accéder au Dashboard Exoplanètes](https://dashboard-tp.streamlit.app)**

---

## Dashboard

Le dashboard permet d'explorer les données grâce à deux filtres interactifs :

- période de découverte ;
- une ou plusieurs méthodes de détection.

Les indicateurs et graphiques sont automatiquement actualisés selon la sélection de l'utilisateur.

Le dashboard contient trois vues principales :

**Population observée** — répartition des exoplanètes par type planétaire.

**Méthodes de détection** — évolution cumulée des découvertes selon les principales méthodes.

**Évolution dans le temps** — nombre de découvertes par année et mise en évidence du pic de découvertes.

Une page complémentaire **Détail des exoplanètes** permet d'explorer le catalogue de manière plus détaillée selon la méthode de détection et le type planétaire.

---

## Contenu du repository

```text
Dashboard/
│
├── app.py
│   └── Application principale Streamlit
│
├── pages/
│   └── 1_Detail_exoplanetes.py
│       └── Vue détaillée des exoplanètes
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

## Documentation

Les choix de conception du dashboard, le message principal, l'audience cible, les KPIs et la justification des visualisations sont détaillés dans :

`cadrage.md`
