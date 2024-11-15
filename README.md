# Application de Gestion des Étudiants avec Flask

Cette application permet de gérer des étudiants, leurs informations et leurs notes. Elle est construite avec **Flask** pour le backend et utilise **Tailwind CSS** pour le style.

## Fonctionnalités

- **Ajout d'étudiant** : Permet d'ajouter un étudiant avec son nom, âge et identifiant.
- **Liste des étudiants** : Affiche tous les étudiants enregistrés avec leurs informations de base et la moyenne de leurs notes.
- **Détails d'un étudiant** : Affiche les informations complètes d'un étudiant, y compris ses notes.
- **Ajout de notes** : Permet d'ajouter des notes pour chaque matière et de marquer un étudiant comme absent (note "abs").
- **Modification d'un étudiant** : Permet de modifier les informations d'un étudiant (nom, âge, identifiant).
- **Suppression d'un étudiant** : Permet de supprimer un étudiant de la liste.

## Prérequis

- Python 3.x
- Flask
- Tailwind CSS (via CDN ou fichier CSS généré)

## Installation


1. **Cloner le repository** :

git clone https://github.com/AxelCF/gestion-etudiants.git
cd gestion-etudiants


2. Créer un environnement virtuel :

python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate


3. Installer les dépendances :

pip install -r requirements.txt



## Lancer l'application

1. Lancer le serveur Flask :

python app.py

Accédez à l'application dans votre navigateur à l'adresse : http://127.0.0.1:5000/.



Structure du projet

gestion-etudiants/
│
├── app.py                # Code backend Flask
├── templates/            # Templates HTML
│   ├── base.html         # Template de base (avec le header et footer communs)
│   ├── index.html        # Page d'accueil
│   ├── ajouter.html      # Formulaire pour ajouter un étudiant
│   ├── etudiants.html    # Liste des étudiants
│   ├── details.html      # Détails d'un étudiant
│   └── modifier.html     # Formulaire pour modifier un étudiant
│
├── static/               # Fichiers statiques (CSS, JS)
│   └── tailwind.css      # Fichier CSS généré par Tailwind ou utilisé via CDN
│
└── requirements.txt      # Liste des dépendances Python


## Fonctionnement

Ajouter un étudiant

1. Sur la page d'accueil, entrez le nom, l'âge et l'identifiant d'un étudiant.

2. Cliquez sur "Ajouter" pour enregistrer l'étudiant dans la base de données (stockée en mémoire).


Afficher la liste des étudiants

1. Accédez à la liste des étudiants.

2. Chaque étudiant est affiché avec son nom, son âge et sa moyenne des notes. La moyenne est calculée uniquement sur les notes valides (en excluant les absences).


Ajouter des notes à un étudiant

1. Pour chaque étudiant, vous pouvez ajouter une note pour une matière.

2. Si l'étudiant est absent, cochez la case "Absent". La note sera alors définie sur "abs".

3. Sinon, entrez une note numérique (entre 0 et 20).


Modifier un étudiant

1. Vous pouvez modifier les informations (nom, âge) d'un étudiant existant en accédant à ses détails et en cliquant sur "Modifier".


Supprimer un étudiant

1. Vous pouvez supprimer un étudiant de la liste en accédant à ses détails et en cliquant sur "Supprimer".


Exemple d'utilisation

1. Ajoutez un étudiant avec le nom "John Doe", l'âge "20", et l'ID "1".

2. Allez dans les détails de "John Doe" et ajoutez des notes pour différentes matières. Par exemple :

	- Mathématiques : 15
	- Physique : 12


3. Si l'élève est absent à un contrôle, cochez "Absent" et ajoutez le comme une note "abs".

4. Vous pouvez voir la moyenne des notes de l'étudiant, qui sera calculée en fonction des notes validées et en excluant les absences.


Auteur : [MAURICE Axel]
Date : Novembre 2024
