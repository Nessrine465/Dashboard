# Document de cadrage — Dashboard Exoplanètes

## 1. Message clé

**Les méthodes de détection façonnent notre vision des exoplanètes : elles ne contribuent pas de la même manière à la population observée et leur évolution a profondément modifié le rythme des découvertes.**

Le dashboard vise à montrer que la population d'exoplanètes actuellement connue dépend en partie des techniques utilisées pour les détecter et de leur évolution dans le temps.

L'objectif n'est donc pas uniquement de présenter le nombre d'exoplanètes découvertes, mais de montrer comment les méthodes d'observation influencent la population que nous connaissons aujourd'hui.

---

## 2. Audience cible

Le dashboard s'adresse à un **public scientifique non spécialiste**, notamment à des étudiants souhaitant comprendre comment les techniques d'observation influencent notre connaissance actuelle des exoplanètes.

L'objectif est de restituer les principaux résultats de l'analyse exploratoire de manière simple, visuelle et interactive, sans nécessiter l'exploration directe des données brutes.

---

## 3. KPIs retenus

### KPI 1 — Exoplanètes observées

Nombre d'exoplanètes correspondant aux filtres sélectionnés.

Pris seul, cet indicateur représente principalement un volume. Il est donc contextualisé par la part du catalogue étudié correspondant à la sélection ainsi que par la période choisie.

Il permet à l'utilisateur de connaître immédiatement la taille de la population sur laquelle portent les visualisations.

### KPI 2 — Méthode de détection dominante

Méthode ayant permis de détecter le plus grand nombre d'exoplanètes dans la sélection.

L'indicateur est accompagné de la part des découvertes correspondant à cette méthode.

Il permet d'identifier rapidement la technique la plus représentée et de vérifier comment cette domination évolue lorsque l'utilisateur modifie la période ou les méthodes sélectionnées.

### KPI 3 — Type planétaire dominant

Type planétaire le plus représenté parmi les exoplanètes classifiées dans la sélection.

L'indicateur est accompagné de sa part dans la population classifiée.

Il permet d'identifier rapidement le profil planétaire dominant et d'observer si sa représentation évolue selon les filtres appliqués.

---

## 4. Structure du dashboard

Le dashboard suit une logique de **storytelling progressif** : partir d'une vue synthétique de la population observée, comprendre le rôle des méthodes de détection, puis observer leur évolution dans le temps.

### Zone 1 — Vue d'ensemble

Trois indicateurs sont présentés en premier :

- nombre d'exoplanètes observées ;
- méthode de détection dominante ;
- type planétaire dominant.

Ces indicateurs sont automatiquement recalculés selon les filtres sélectionnés.

### Zone 2 — Population observée

Un diagramme en barres présente la répartition des exoplanètes selon quatre catégories :

- Rocheuse ;
- Super-Terre / Mini-Neptune ;
- Neptunienne ;
- Géante gazeuse.

La catégorie la plus représentée est mise en évidence afin de faciliter la lecture du graphique.

Cette visualisation permet d'identifier rapidement la structure de la population d'exoplanètes observée.

### Zone 3 — Méthodes de détection

Un graphique temporel présente le nombre cumulé de découvertes pour les principales méthodes de détection.

Il permet de comparer leur contribution au catalogue d'exoplanètes et d'observer comment leur importance évolue dans le temps.

### Zone 4 — Évolution des découvertes

Un graphique en courbe présente le nombre d'exoplanètes découvertes chaque année.

L'année présentant le plus grand nombre de découvertes dans la sélection est mise en évidence.

Cette visualisation permet d'identifier les périodes d'accélération des découvertes et de les comparer selon les méthodes sélectionnées.

---

## 5. Filtres interactifs

La sidebar contient deux filtres principaux :

- **période de découverte** ;
- **méthodes de détection**.

Le filtre sur les méthodes permet de sélectionner une, plusieurs ou toutes les méthodes disponibles.

Les trois KPIs et les trois visualisations réagissent aux filtres sélectionnés.

Cette interactivité permet à l'utilisateur de tester le message du dashboard sur différentes périodes et différentes populations.

---

## 6. Justification des visualisations

### Diagramme en barres — Répartition par type planétaire

Le diagramme en barres est adapté à la comparaison de catégories.

Il permet de comparer directement le nombre d'exoplanètes appartenant à chaque type planétaire et d'identifier rapidement les catégories les plus et les moins représentées.

### Courbes cumulées — Méthodes de détection

Une représentation temporelle cumulée permet de comparer la contribution des principales méthodes de détection au catalogue d'exoplanètes.

Elle met en évidence les différences de rythme et de volume de découvertes entre les méthodes.

### Courbe temporelle — Découvertes annuelles

La courbe temporelle est adaptée à l'analyse de l'évolution du nombre de découvertes au fil des années.

Elle permet d'identifier les phases d'accélération ainsi que l'année présentant le plus grand nombre de découvertes dans la période sélectionnée.

Ces trois visualisations répondent au même message :

**notre vision de la population d'exoplanètes dépend en partie des techniques utilisées pour les détecter et de leur évolution dans le temps.**

---

## 7. Choix de design et hiérarchie visuelle

Le dashboard adopte une structure volontairement simple afin de limiter la charge cognitive.

La hiérarchie de lecture est la suivante :

1. message principal ;
2. KPIs de synthèse ;
3. population observée ;
4. comparaison des méthodes ;
5. évolution temporelle.

Les titres des visualisations sont formulés comme des messages afin d'accompagner l'utilisateur dans la lecture des résultats.

Les couleurs sont utilisées avec parcimonie pour mettre en évidence les informations importantes, notamment la catégorie dominante ou le pic de découvertes.

---

## 8. Conclusion 

Le dashboard doit permettre de mettre en évidence que la population d'exoplanètes actuellement connue ne peut pas être interprétée indépendamment des techniques utilisées pour la détecter.

La répartition des types planétaires fournit une première vision de la population observée.

La comparaison des méthodes de détection montre que certaines techniques contribuent beaucoup plus fortement que d'autres au catalogue connu.

Enfin, l'évolution annuelle des découvertes met en évidence des périodes de forte accélération.

L'interactivité permet à l'utilisateur de modifier la période et les méthodes sélectionnées afin de vérifier comment ces constats évoluent.

L'objectif final est ainsi de montrer que **la population d'exoplanètes actuellement connue est en partie façonnée par les méthodes et les technologies utilisées pour les détecter.**