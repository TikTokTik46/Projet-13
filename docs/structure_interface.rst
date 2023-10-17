V. Structure des interfaces de programmation
--------------------------------------------

Ce projet Django repose sur un ensemble d'interfaces de programmation (API) soigneusement conçues, qui constituent le pilier de notre stack technologique. Elles jouent un rôle central dans la gestion, la collaboration et le déploiement harmonieux de notre application, assurant un flux de travail fluide et efficace de bout en bout.

GitHub
~~~~~~

GitHub est une plateforme en ligne qui permet aux développeurs de stocker, gérer et collaborer sur leurs projets de développement de logiciels. Elle offre des outils de gestion de code source, de suivi des problèmes, de documentation et de collaboration, rendant le travail en équipe plus efficace. Les développeurs peuvent héberger leurs projets, partager des ressources et contribuer à d'autres projets open source.

C’est à partir de la création de demande de fusion du code modifié via GitHub que notre processus de d’intégration continue est lancé.

CircleCI
~~~~~~~~

CircleCI est une plateforme d'intégration continue qui automatise le processus de construction, de test et de déploiement des logiciels. Elle permet aux équipes de développement de détecter rapidement les erreurs, d'assurer la qualité du code et de livrer des applications fiables. CircleCI prend en charge de nombreux langages de programmation, environnements et intégrations tierces pour une personnalisation maximale du pipeline d'intégration continue.

Le fichier ``config.yml`` permet de configurer les étapes du workflow de notre processus d’intégration continue, celui-ci est déclenché à chaque push ou pull request sur la branche master.

.. literalinclude:: ../.circleci/config.yml
   :language: yaml
   :linenos:
   :caption: Fichier de configuration CircleCI (config.yml)

Docker
~~~~~~

Docker est une plateforme de conteneurisation qui révolutionne la manière dont les applications sont développées, déployées et gérées. Elle permet d'emballer des applications et leurs dépendances dans des conteneurs légers et portables, assurant une uniformité et une reproductibilité de l'environnement d'exécution. Docker simplifie le développement, l'intégration et le déploiement d'applications, offrant une plus grande flexibilité pour les équipes de développement.

Le fichier ``Dockerfile`` permet de préciser les étapes permettant la création de notre image.

.. literalinclude:: ../Dockerfile
   :language: Dockerfile
   :linenos:
   :caption: Fichier de configuration de la création de l'image (Dockerfile)

Ce fichier utilise une image Python de base, configure l'environnement, récupère la clé secrète en tant qu'argument, définit le répertoire de travail, copie les dépendances et le code source, installe les dépendances, collecte les fichiers statiques, expose le port 8000, et exécute l'application avec Gunicorn.

Afin de pouvoir déployer notre application en ligne, nous faisons un pull de cette image sur le cloud DockerHub. Cette image est ensuite transmise à Render pour son déploiement.

Sentry
~~~~~~

Sentry est un service de gestion d'erreurs qui permet de suivre, de signaler et de résoudre les bogues et les problèmes dans les applications en temps réel. En fournissant une meilleure visibilité sur la qualité du logiciel, Sentry aide les développeurs à identifier, comprendre et corriger rapidement les erreurs, améliorant ainsi l'expérience utilisateur.

L’intégration et la configuration de Sentry dans l’application Django à été réalisé dans le fichier ``settings.py``.

Render
~~~~~~

Render est une plateforme de cloud computing qui simplifie le déploiement d'applications. Elle offre un environnement évolutif et hautement performant pour les développeurs, sans la nécessité de gérer les détails complexes de l'infrastructure. Render prend en charge une variété de langages de programmation, de bases de données et de services, permettant aux développeurs de se concentrer sur le développement de leurs applications plutôt que sur l'administration des serveurs. Cette plateforme propose un déploiement simple et des mises à jour continues, offrant ainsi une expérience fluide pour les développeurs et les utilisateurs finaux.

Comme précisé précédemment, un lien a été créé entre notre Docker Hub et Render afin que le déploiement soit réalisé automatiquement à chaque mise à jour de l’image.
