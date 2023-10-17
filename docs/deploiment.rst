VII. Déploiement et gestion de l'application
--------------------------------------------
Pour réaliser le déploiement de l'application via le pipeline CI/CD, vous devez créer des comptes sur CircleCI (https://circleci.com/) et Render (https://render.com/), en plus des comptes GitHub et Docker créés précédemment.

Configuration de CircleCI
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connectez-vous à votre compte CircleCI :
   - Connectez-vous à votre compte CircleCI avec vos identifiants.

2. Autorisez l'accès à GitHub et configurez votre projet :
   - Une fois connecté à CircleCI, cliquez sur le menu en haut à droite et sélectionnez "User Settings" (Paramètres de l'utilisateur).
   - Dans le menu de gauche, cliquez sur "Organization."
   - Sous "Add an Organization," sélectionnez l'organisation GitHub que vous souhaitez connecter. Si vous ne voyez pas votre organisation, assurez-vous que votre compte GitHub dispose des autorisations appropriées.
   - Cliquez sur "Authorize with GitHub" (Autoriser avec GitHub) et suivez les étapes pour autoriser l'accès de CircleCI à votre compte GitHub.
   - Après avoir autorisé l'accès, vous pouvez maintenant configurer un projet pour une intégration continue avec CircleCI. Dans la page d'accueil de votre compte CircleCI, cliquez sur "Add Projects" (Ajouter des projets).

3. Ajoutez vos variables d'environnement
   - Il est ensuite nécessaire d'ajouter les variables d'environnement pour le bon fonctionnement de CircleCI. Pour ce faire, ajoutez les variables SECRET_KEY (Clé secrète du projet Django), DOCKER_USERNAME (Nom de votre compte DockerHub) et DOCKER_PASSWORD (Mot de passe de votre compte DockerHub).

Configuration de DockerHub
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour réaliser le push de l'image vers votre DockerHub, il est nécessaire de modifier le fichier *config.yml* en remplaçant "nomdevotrecompte" par le nom de votre compte dans le job **build_docker_image**.

   .. code-block:: yaml

      build_docker_image:  # Construction de l'image et push vers Docker Hub
        executor: python/default
        steps:
          - checkout
          - setup_remote_docker: # Utilise remote Docker executor !
              version: 20.10.14
              docker_layer_caching: true
          - run:
              name: Build Docker image
              command: docker build --build-arg SECRET_KEY=$SECRET_KEY -t nomdevotrecompte/oc-lettings:latest .
          - run:
              name: Push Docker image to Docker Hub
              command: |
                echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                docker push nomdevotrecompte/oc-lettings:latest


Configuration de Render
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour déployer l'application depuis DockerHub sur Render, connectez-vous à Render et créez un nouveau service web en spécifiant l'environnement Docker et en fournissant le chemin complet de l'image DockerHub à déployer. Configurez les ports d'écoute et définissez la variable d'environnement "SECRET_KEY". Une fois le service web configuré, vous obtiendrez une adresse Hook qu'il vous faudra lier à votre compte DockerHub pour permettre un déploiement continu à chaque mise à jour de l'image. Render se chargera du déploiement de l'application, et une fois terminé, vous pourrez y accéder via le lien fourni dans votre tableau de bord Render.