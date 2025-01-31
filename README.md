# 🏆 Gestion de Tournoi d'Échecs

Ce projet est une application Python permettant de gérer des tournois d'échecs en générant des rounds et en organisant les matchs entre les joueurs.

---

## 📌 Fonctionnalités

- 🎯 Ajout des joueurs
- 🎯 Création d'un tournoi
- 🎯 Création et organisation des rounds
- 🎯 Éviter les matchs en double entre joueurs
- 🎯 Gestion des matchs et résultats
- 🎯 Sauvegarde et chargement des données

---

## 🛠️ Technologies Utilisées

- 🐍 Python 3.13
- 📦 Typage avec `typing`
- 📂 Gestion des fichiers JSON
- ✅ Respect des bonnes pratiques PEP8 avec `flake8`

---

## 📦 Structure du Projet

```
📦 Club-Echec
│-- 📂 Controller
│   ├── Match_controller.py  # Gestion des matchs
│   ├── Round_controller.py  # Gestion des rounds
│   ├── Tournament_controller.py  # Gestion des tournois
│   ├── Player_controller.py  # Gestion des joueurs
│-- 📂 Model
│   ├── Player.py  # Modèle des joueurs
│   ├── Match.py   # Modèle des matchs
│   ├── Round.py   # Modèle des rounds
│   ├── Tournament.py  # Modèle des tournois
│-- 📂 View
│   ├── menu_view.py  # Interface en console
│   ├── home_view.py  # Vue d'accueil
│   ├── add_player_view.py  # Interface pour ajouter un joueur
│   ├── add_tournament_view.py  # Interface pour ajouter un tournoi
│   ├── all_players_view.py  # Affichage de tous les joueurs
│   ├── all_tournaments_view.py  # Affichage de tous les tournois
│   ├── report_menu_view.py  # Menu pour les rapports
│   ├── show_tournament_players_view.py  # Affichage des joueurs d'un tournoi
│   ├── show_tournament_rounds_view.py  # Affichage des rounds d'un tournoi
│   ├── tournaments_menu_view.py  # Menu des tournois
│-- 📂 Utils
│   ├── save_to_JSON.py  # Sauvegarde des données
│   ├── load_from_JSON.py  # Chargement des données
│-- 📂 data
│   ├── tournaments.json  # Données des tournois
│   ├── players.json  # Données des joueurs
│-- 📂 Exception
│   ├── Player_exception.py  # Exceptions liées aux joueurs
│   ├── Tournament_exception.py  # Exceptions liées aux tournois
│-- 📂 flake8-report  # Dossier contenant le rapport Flake8
│   ├── report.txt  # Rapport d'analyse de code avec Flake8
│-- 📂 Validator
│   ├── player_validator.py  # Validation des joueurs
│   ├── exception_validator.py  # Validation des exceptions
│-- .idea/  # Dossier de configuration PyCharm
│-- main.py  # Point d'entrée du programme
│-- README.md  # Documentation
│-- requirements.txt  # Liste des dépendances
│-- .gitignore  # Fichiers à ignorer dans Git
```

---

## 🚀 Installation et Exécution

### 1️⃣ Installation

1. Clone ce dépôt :
   ```sh
   git clone https://github.com/ton-projet.git
   cd Club-Echec
   ```
2. Crée un environnement virtuel et active-le :
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # Sur Linux/Mac
   .venv\Scripts\activate     # Sur Windows
   ```
3. Installe les dépendances :
   ```sh
   pip install -r requirements.txt
   ```

### 2️⃣ Exécution du programme

Lance l'application avec :
```sh
python main.py
```

---

## 📞 Contact

- 👨‍💻 **Auteur** : Marc
- 🎓 **Supervision** : OpenClassrooms
- 🔗 **Dépôt GitHub** : [Lien du projet](https://github.com/Youorus/Python-ChessClub)

---


