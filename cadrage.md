# Document de cadrage — Dashboard Exoplanètes

## 1. Message clé

**Les méthodes de détection façonnent notre vision des exoplanètes : elles ne contribuent pas de la même manière à la population observée et leur évolution a profondément modifié le rythme des découvertes.**

Le dashboard vise à montrer que la population d'exoplanètes actuellement connue dépend en partie des techniques utilisées pour les détecter et de leur évolution dans le temps.

L'objectif n'est donc pas uniquement de présenter le nombre d'exoplanètes découvertes, mais de montrer comment les méthodes de détection influencent la population que nous connaissons aujourd'hui.

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

Il permet d'identifier rapidement la technique la plus représentée et d'observer comment cette domination évolue lorsque l'utilisateur modifie la période ou les méthodes sélectionnées.

### KPI 3 — Type planétaire dominant

Type planétaire le plus représenté parmi les exoplanètes classifiées dans la sélection.

L'indicateur est accompagné de sa part dans la population classifiée.

Il permet d'identifier rapidement le profil planétaire dominant et d'observer si sa représentation évolue selon les filtres appliqués.

---

## 4. Structure du dashboard

Le dashboard suit une logique de **storytelling progressif** : partir d'une vue synthétique de la population observée, comprendre le rôle des méthodes de détection, puis observer l'évolution des découvertes dans le temps.

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

La catégorie la plus représentée est mise en évidence en vert, la moins représentée en rouge et les catégories intermédiaires en gris, afin de faciliter la comparaison visuelle des extrêmes.

Cette visualisation permet d'identifier rapidement la structure de la population d'exoplanètes observée et de vérifier si cette répartition évolue lorsque les filtres sont modifiés.

### Zone 3 — Méthodes de détection

Un graphique temporel présente le nombre cumulé de découvertes pour les quatre méthodes de détection les plus représentées dans la sélection.

Il permet de comparer leur contribution au catalogue d'exoplanètes et d'observer comment leur importance évolue dans le temps.

### Zone 4 — Évolution des découvertes

Un graphique en courbe présente le nombre d'exoplanètes découvertes chaque année.

L'année présentant le plus grand nombre de découvertes dans la période sélectionnée est mise en évidence par un point vert.

Cette visualisation permet d'identifier les principales périodes d'accélération des découvertes et d'observer comment celles-ci évoluent selon les méthodes sélectionnées.

---

## 5. Filtres interactifs

La sidebar contient deux filtres principaux :

- **période de découverte** ;
- **méthodes de détection**.

Le filtre sur les méthodes permet de sélectionner une, plusieurs ou toutes les méthodes disponibles.

Les KPIs et les visualisations sont automatiquement recalculés selon les filtres sélectionnés.

Cette interactivité permet à l'utilisateur d'explorer différentes périodes et différentes méthodes et d'observer directement leur effet sur les résultats présentés.

---

## 6. Justification des visualisations

### Diagramme en barres — Répartition par type planétaire

Le diagramme en barres est adapté à la comparaison de catégories.

Il permet de comparer directement le nombre d'exoplanètes appartenant à chaque type planétaire et d'identifier rapidement les catégories les plus et les moins représentées.

L'utilisation de couleurs distinctes pour les valeurs extrêmes facilite la lecture tout en conservant une représentation simple.

### Courbes cumulées — Méthodes de détection

Une représentation temporelle cumulée permet de comparer la contribution des principales méthodes de détection au catalogue d'exoplanètes.

Elle met en évidence les différences de rythme et de volume de découvertes entre les méthodes au fil du temps.

### Courbe temporelle — Découvertes annuelles

La courbe temporelle est adaptée à l'analyse de l'évolution du nombre de découvertes au fil des années.

Elle permet d'identifier les phases d'accélération ainsi que l'année présentant le plus grand nombre de découvertes dans la période sélectionnée.

Le pic est volontairement mis en évidence afin d'attirer l'attention sur cette information importante.

Ces trois visualisations contribuent au même message :

**notre vision de la population d'exoplanètes dépend en partie des techniques utilisées pour les détecter et de leur évolution dans le temps.**

---

## 7. Choix de design et hiérarchie visuelle

Le dashboard adopte une structure volontairement simple afin de limiter la charge cognitive et de faciliter la compréhension des résultats.

La hiérarchie de lecture est la suivante :

1. message principal ;
2. KPIs de synthèse ;
3. population observée ;
4. comparaison des méthodes de détection ;
5. évolution des découvertes dans le temps.

Les visualisations sont organisées dans des onglets afin de séparer les différentes étapes de l'analyse tout en conservant une navigation simple.

Les titres des visualisations sont formulés comme des messages afin d'accompagner l'utilisateur dans la lecture et de renforcer le storytelling.

Les couleurs sont utilisées avec parcimonie pour mettre en évidence les informations importantes sans surcharger les graphiques.

---

## 8. Interactivité et storytelling

L'interactivité constitue une partie essentielle du dashboard.

L'utilisateur peut modifier la période d'analyse et sélectionner une ou plusieurs méthodes de détection. Les KPIs, les textes d'accompagnement et les visualisations sont alors actualisés selon la sélection.

Le storytelling suit trois étapes :

1. **Observer la population connue** en identifiant les types planétaires les plus représentés ;
2. **Comparer les méthodes de détection** afin d'observer leur contribution respective aux découvertes ;
3. **Analyser l'évolution dans le temps** afin d'identifier les principales phases d'accélération des découvertes.

Cette organisation permet de passer progressivement d'une vue générale de la population à une analyse temporelle des découvertes.

---

## 9. Conclusion attendue

Le dashboard doit permettre de mettre en évidence que la population d'exoplanètes actuellement connue ne peut pas être interprétée indépendamment des techniques utilisées pour la détecter.

La répartition des types planétaires fournit une première vision de la population observée.

La comparaison des méthodes de détection montre que les différentes techniques ne contribuent pas dans les mêmes proportions au catalogue connu.

Enfin, l'évolution annuelle des découvertes permet d'identifier des périodes de forte accélération.

Grâce aux filtres interactifs, l'utilisateur peut modifier la période et les méthodes sélectionnées afin d'observer comment ces constats évoluent.

L'objectif final est ainsi de montrer que **la population d'exoplanètes actuellement connue est en partie façonnée par les méthodes et les technologies utilisées pour les détecter.**