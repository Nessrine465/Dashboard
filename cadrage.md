# Document de cadrage — Dashboard Exoplanètes

## 1. Message clé

**Les méthodes de détection façonnent notre vision des exoplanètes : elles ne permettent pas toutes d'observer les mêmes types de planètes et leur évolution a progressivement élargi les populations que nous sommes capables de détecter.**

Le dashboard vise à montrer que les caractéristiques des exoplanètes connues dépendent en partie des méthodes utilisées pour les détecter et de leur évolution dans le temps.

## 2. Audience cible

Le dashboard s'adresse à un **public scientifique non spécialiste**, notamment des étudiants souhaitant comprendre comment les techniques d'observation influencent notre connaissance actuelle des exoplanètes.

L'objectif est de restituer les principaux résultats de l'analyse exploratoire de manière simple, visuelle et interactive, sans nécessiter l'exploration des données brutes.

## 3. KPIs retenus

### KPI 1 — Nombre d'exoplanètes découvertes

Nombre d'exoplanètes correspondant aux filtres sélectionnés.

Pris seul, cet indicateur peut être considéré comme une **vanity metric**, car il représente principalement un volume. Il devient plus pertinent lorsqu'il est contextualisé par la période et la méthode de découverte sélectionnées.

### KPI 2 — Méthode de découverte dominante

Méthode ayant permis de détecter le plus grand nombre d'exoplanètes dans la sélection.

Cet indicateur est **actionnable pour l'analyse**, car il permet d'identifier immédiatement quelle technique contribue le plus à la population observée.

### KPI 3 — Rayon médian des exoplanètes

Rayon médian des exoplanètes sélectionnées, exprimé en rayons terrestres (R⊕).

La médiane est privilégiée à la moyenne afin de limiter l'influence des valeurs extrêmes. Sa comparaison entre différentes méthodes ou périodes permet d'observer l'évolution du profil des planètes détectées.

## 4. Structure du dashboard

Le dashboard sera organisé de manière à faire apparaître l'information essentielle en premier, puis à permettre à l'utilisateur d'approfondir l'analyse.

### Zone 1 — KPIs

Trois indicateurs seront visibles immédiatement :

- nombre d'exoplanètes découvertes ;
- méthode de découverte dominante ;
- rayon médian.

Ils seront automatiquement recalculés selon les filtres sélectionnés.

### Zone 2 — Évolution des découvertes par méthode

Une visualisation temporelle présentera l'évolution des découvertes selon les principales méthodes de détection.

Elle permettra d'observer comment l'importance des différentes techniques de découverte a évolué dans le temps.

### Zone 3 — Caractéristiques des planètes selon la méthode

Des boxplots permettront de comparer les caractéristiques des exoplanètes détectées selon leur méthode de découverte :

- rayon ;
- période orbitale ;
- distance.

Cette visualisation permettra de montrer que les différentes méthodes ne détectent pas nécessairement les mêmes populations de planètes.

### Zone 4 — Évolution du rayon médian par méthode et décennie

Une heatmap représentera le rayon médian des exoplanètes selon la méthode de découverte et la décennie.

Elle permettra de visualiser simultanément l'effet du temps et de la méthode sur les caractéristiques des planètes découvertes.

## 5. Filtres interactifs

La sidebar contiendra au minimum deux filtres :

- **période de découverte** ;
- **méthode de découverte**.

Les KPIs et les visualisations réagiront aux filtres afin de permettre à l'utilisateur de comparer différentes populations d'exoplanètes.

## 6. Justification des visualisations

**Graphique temporel :** adapté à une donnée chronologique, il permet d'identifier rapidement les évolutions et changements dans les méthodes de découverte.

**Boxplots :** adaptés à la comparaison de distributions, ils permettent de comparer la médiane, la dispersion et les valeurs extrêmes des caractéristiques des planètes selon leur méthode de découverte.

**Heatmap :** adaptée à une comparaison croisée entre deux dimensions catégorielles, elle permet d'identifier rapidement les différences de rayon médian selon les méthodes et les décennies.

Ces trois visualisations ont été retenues car elles contribuent toutes au même message : **la population d'exoplanètes que nous observons dépend des techniques utilisées pour les détecter et de leur évolution dans le temps.**

## 7. Conclusion attendue

Le dashboard doit permettre de mettre en évidence que les exoplanètes observées ne présentent pas les mêmes caractéristiques selon les méthodes utilisées pour les détecter.

L'évolution des découvertes dans le temps, la comparaison des caractéristiques physiques des planètes selon les méthodes de détection et l'évolution du rayon médian par décennie permettront d'illustrer les biais liés aux techniques d'observation.

L'objectif final est ainsi de montrer que **la population d'exoplanètes actuellement connue est en partie façonnée par les méthodes et les technologies utilisées pour les détecter**.