IV. Structure de la base de données et des modèles
-----------------------------------------------------

Base de données SQLite
~~~~~~~~~~~~~~~~~~~~~~~

Pour stocker les diverses informations, nous avons opté pour l'utilisation d'une base de données SQLite. Ce système de gestion de base de données relationnelle, léger, est à la fois rapide et fiable. Il s'agit d'un choix courant pour les applications requérant une petite empreinte de base de données et une configuration simplifiée.

Structure de la base de données
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plusieurs modèles ont été créés pour organiser nos données. Voici une brève description de ces modèles.

**User (Utilisateur)**

Modèle natif de Django permettant de définir les utilisateurs. Ce modèle est notament utilisé pour accéder à l'interface d'administration.

**Profile (Profil)**

- id: Identifiant unique du profil.
- user: Clé étrangère liée à la table User, identifiant de l'utilisateur propriétaire du profil.
- favorite_city: La ville favorite de l'utilisateur (facultatif).

**Address (Adresse)**

- id: Identifiant unique de l'adresse.
- number: Numéro de rue.
- street: Nom de la rue.
- city: Ville.
- state: État ou province.
- zip_code: Code postal.
- country_iso_code: Code ISO du pays.

**Letting (Location)**

- id: Identifiant unique de la location.
- title: Titre de la location.
- address: Clé étrangère liée à la table Adresse, identifiant de l'adresse associée à la location.

Cette structure de base de données permet d'organiser efficacement les informations relatives aux utilisateurs, aux profils, aux adresses et aux locations dans notre application.
